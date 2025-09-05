/*
* TWAIN32 Configuration Manager
*
* Copyright 2025 Ivan Lyugaev
*
* This library is free software; you can redistribute it and/or
* modify it under the terms of the GNU Lesser General Public
* License as published by the Free Software Foundation; either
* version 2.1 of the License, or (at your option) any later version.
*
* This library is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
* Lesser General Public License for more details.
*
* You should have received a copy of the GNU Lesser General Public
* License along with this library; if not, write to the Free Software
* Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA
*/

#include <stdio.h>
#include <stdlib.h>
#include "wine/debug.h"

#include "cfg.h"

WINE_DEFAULT_DEBUG_CHANNEL( twain );

LSTATUS get_info_key( WCHAR* path, HKEY* h_key, DWORD* dispos )
{
    WCHAR reg_path[MAX_PATH];
    swprintf( reg_path, MAX_PATH, L"Software\\ScannersSettings\\%s", path );

    return RegCreateKeyExW(
        HKEY_CURRENT_USER,
        reg_path,
        0,
        NULL,
        REG_OPTION_NON_VOLATILE,
        KEY_ALL_ACCESS,
        NULL,
        h_key,
        dispos
    );
}

BOOL save_to_reg( WCHAR* path, DWORD reg_type, CHAR* name, const BYTE* value, DWORD size )
{
    HKEY h_key;
    DWORD dispos;
    LSTATUS res;

    res = get_info_key(path, &h_key, &dispos);

    if( res != ERROR_SUCCESS )
    {
        ERR( "RegCreateKeyExW: %ld\n", res );
        return FALSE;
    }

    res = RegSetValueExA(
        h_key,
        name,
        0,
        reg_type,
        value,
        size
    );

    RegCloseKey( h_key );

    if ( res != ERROR_SUCCESS ) {
        ERR( "RegSetValueExA error: %ld\n", res );
        return FALSE;
    }

    return TRUE;
}

BOOL load_from_reg( WCHAR* path, int opt_type, CHAR* name, void* value )
{
    HKEY h_key;
    DWORD dispos, flag, size;
    LSTATUS res;

    res = get_info_key(path, &h_key, &dispos);

    if( res != ERROR_SUCCESS )
    {
        ERR( "RegCreateKeyExW: %ld\n", res );
        return FALSE;
    }

    switch( opt_type )
    {
        case TYPE_INT:
        case TYPE_FIXED:
        case TYPE_BOOL:
            flag = RRF_RT_REG_DWORD;
            size = sizeof(DWORD);
            break;
        case TYPE_STRING:
            flag = RRF_RT_REG_SZ;
            size = OPTION_VALUE_MAX;
            break;
        default:
            RegCloseKey( h_key );
            ERR( "Unknown type: %d\n", opt_type );
            return FALSE;
    }

    res = RegGetValueA(
        h_key,
        NULL,
	name,
	flag,
	NULL,
        value,
	&size
    );

    RegCloseKey( h_key );

    return res == ERROR_SUCCESS;
}
