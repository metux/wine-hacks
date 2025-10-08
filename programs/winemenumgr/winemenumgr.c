#include <windows.h>
#include <stdio.h>

HINSTANCE inst;
HWND hListBox[2];

HWND ListBox1 (HWND hwnd)
{
HWND hListBox=CreateWindow(
                        "LISTBOX","",
                         WS_VISIBLE|WS_CHILD|WS_BORDER |LBS_NOTIFY |LBS_COMBOBOX,
                         10,10,280,380,hwnd,NULL,inst,NULL);
return hListBox;
}

HWND ListBox2 (HWND hwnd)
{
HWND hListBox=CreateWindow(
                        "LISTBOX","",
                         WS_VISIBLE|WS_CHILD|WS_BORDER |LBS_NOTIFY,
                         400,10,280,380,hwnd,NULL,inst,NULL);

return hListBox;
}

HWND dirright(HWND hwnd,HMENU code,long x, long y, char * texte)
{
HWND hBouton=CreateWindow(
                        "BUTTON",
                        texte,
                        WS_CHILD|WS_VISIBLE|BS_PUSHBUTTON,
                        x,y,
                        90,30,
                        hwnd,
                        code,
                        inst,
                        NULL);
return hBouton;
}
HWND dirleft(HWND hwnd,HMENU code,long x, long y, char * texte)
{
HWND hBouton=CreateWindow(
                        "BUTTON",
                        texte,
                        WS_CHILD|WS_VISIBLE|BS_PUSHBUTTON,
                        x,y,
                        90,30,
                        hwnd,
                        code,
                        inst,
                        NULL);
return hBouton;
}
HWND dirup(HWND hwnd,HMENU code,long x, long y, char * texte)
{
HWND hBouton=CreateWindow(
                        "BUTTON",
                        texte,
                        WS_CHILD|WS_VISIBLE|BS_PUSHBUTTON,
                        x,y,
                        90,30,
                        hwnd,
                        code,
                        inst,
                        NULL);
return hBouton;
}
HWND dirdown(HWND hwnd,HMENU code,long x, long y, char * texte)
{
HWND hBouton=CreateWindow(
                        "BUTTON",
                        texte,
                        WS_CHILD|WS_VISIBLE|BS_PUSHBUTTON,
                        x,y,
                        90,30,
                        hwnd,
                        code,
                        inst,
                        NULL);
return hBouton;
}
HWND modify(HWND hwnd,HMENU code,long x, long y, char * texte)
{
HWND hBouton=CreateWindow(
                        "BUTTON",
                        texte,
                        WS_CHILD|WS_VISIBLE|BS_PUSHBUTTON,
                        x,y,
                        90,30,
                        hwnd,
                        code,
                        inst,
                        NULL);
return hBouton;
}
HWND delete(HWND hwnd,HMENU code,long x, long y, char * texte)
{
HWND hBouton=CreateWindow(
                        "BUTTON",
                        texte,
                        WS_CHILD|WS_VISIBLE|BS_PUSHBUTTON,
                        x,y,
                        90,30,
                        hwnd,
                        code,
                        inst,
                        NULL);
return hBouton;
}
HWND ok(HWND hwnd,HMENU code,long x, long y, char * texte)
{
HWND hBouton=CreateWindow(
                        "BUTTON",
                        texte,
                        WS_CHILD|WS_VISIBLE|BS_PUSHBUTTON,
                        x,y,
                        90,30,
                        hwnd,
                        code,
                        inst,
                        NULL);
return hBouton;
}
HWND apply(HWND hwnd,HMENU code,long x, long y, char * texte)
{
HWND hBouton=CreateWindow(
                        "BUTTON",
                        texte,
                        WS_CHILD|WS_VISIBLE|BS_PUSHBUTTON,
                        x,y,
                        90,30,
                        hwnd,
                        code,
                        inst,
                        NULL);
return hBouton;
}
HWND cancel(HWND hwnd,HMENU code,long x, long y, char * texte)
{
HWND hBouton=CreateWindow(
                        "BUTTON",
                        texte,
                        WS_CHILD|WS_VISIBLE|BS_PUSHBUTTON,
                        x,y,
                        90,30,
                        hwnd,
                        code,
                        inst,
                        NULL);
return hBouton;
}


LRESULT CALLBACK  Procedure (HWND hwnd, UINT message, WPARAM wParam, LPARAM lParam)
{

    static HWND hBouton[1]={0};
    char texte[5]={0},texte2[50]={0};
switch (message)

    {
        case WM_CREATE:
               hListBox[0]=ListBox1 (hwnd);
               hListBox[0]=ListBox2 (hwnd);

               hBouton[0]= dirright(hwnd, (HMENU)ID_BOUTON1,300,20, "Right");
               hBouton[0]= dirleft(hwnd, (HMENU)ID_BOUTON2,300,60, "Left");
               hBouton[0]= dirup(hwnd, (HMENU)ID_BOUTON1,300,100, "Up");
               hBouton[0]= dirdown(hwnd, (HMENU)ID_BOUTON2,300,140, "Down");
               hBouton[0]= modify(hwnd, (HMENU)ID_BOUTON3,300,180, "Modify");
               hBouton[0]= delete(hwnd, (HMENU)ID_BOUTON4,300,220, "Delete");
               hBouton[0]= ok(hwnd, (HMENU)ID_BOUTON5,300,260, "Ok");
               hBouton[0]= apply(hwnd, (HMENU)ID_BOUTON6,300,300, "Apply");
               hBouton[0]= cancel(hwnd, (HMENU)ID_BOUTON7,300,340, "Cancel");
        return 0;

        case WM_COMMAND:

          switch (LOWORD(wParam))
          {
              //test du message LB_GETCURSEL
              case ID_BOUTON1 :
               //Trouver le numéro de la ligne sélectionnée, et transformer le résultat en chaîne
               sprintf(texte,"%d",(SendMessage(hListBox[0],LB_GETCURSEL,0,0)+1));
               //Afficher une boîte de dialogue
               //s'il y a une sélection
              if (SendMessage(hListBox[0],LB_GETCURSEL,0,0)!= LB_ERR)
              {
                strncat(texte2,"Vous avez sélectionné la ligne ",50);
                strncat(texte2,texte,50);
              }
              else //pas de sélection
              {
              strncat(texte2,"Vous n'avez sélectionné aucune ligne." ,50);
              }
              MessageBox(hwnd,(LPCTSTR )texte2,"",MB_OK|MB_ICONWARNING);
              break;
              //ajoutez d'autres tests et d'autres boutons si vous le voulez
              //case ID_BOUTON2:
              //autre test
              //breaks;
              case ID_BOUTON2 :
               //Trouver le numéro de la ligne sélectionnée, et transformer le résultat en chaîne
                //Afficher une boîte de dialogue
               //s'il y a une sélection
              if (SendMessage(hListBox[0],LB_GETCURSEL,0,0)!= LB_ERR)
              {
                strncat(texte2,"Vous avez appuyer sur le bouton de d\351placement de l'\351l\351ment vers la gauche", 90);
                strncat(texte2,texte, 90);
              }
              else //pas de sélection
              {
              strncat(texte2,"Pas de sélection", 90);
              }
              MessageBox(hwnd,(LPCTSTR )texte2,"",MB_OK|MB_ICONINFORMATION);
              break;

              case ID_BOUTON3 :
              {
                strncat(texte2,"Vous avez appuyer sur le bouton de modification",90);
                strncat(texte2,texte,90);
              }
              MessageBox(hwnd,(LPCTSTR )texte2,"",MB_OK|MB_ICONINFORMATION);
              break;

              case ID_BOUTON4 :
              {
                strncat(texte2,"Vous avez appuyer sur le bouton de suppression d'une ligne",90);
                strncat(texte2,texte,90);
              }
              MessageBox(hwnd,(LPCTSTR )texte2,"",MB_OK|MB_ICONINFORMATION);
              break;

              case ID_BOUTON5 :
              {
                strncat(texte2,"Vous avez appuyer sur le bouton de confirmation",90);
                strncat(texte2,texte,90);
              }
              MessageBox(hwnd,(LPCTSTR )texte2,"",MB_OK|MB_ICONINFORMATION);
              break;

              case ID_BOUTON6 :
              {
                strncat(texte2,"Vous avez appuyer sur le bouton d'application des modifications",90);
                strncat(texte2,texte,90);
              }
              MessageBox(hwnd,(LPCTSTR )texte2,"",MB_OK|MB_ICONINFORMATION);
              break;

              case ID_BOUTON7:
                DestroyWindow(hwnd);
              break;
              //ajoutez d'autres tests et d'autres boutons si vous le voulez
              //case ID_BOUTON2:
              //autre test
              //breaks;

          }

           switch (HIWORD(wParam))
          {
              case LBN_SELCHANGE :
                char temp[256] = "";
                SendMessage(hListBox, LB_GETTEXT, SendMessage(hListBox[0], LB_GETCURSEL, 0, 0), temp);
                MessageBox(hwnd,temp, "Item sélectionné :", MB_ICONINFORMATION);
              break;
          }
              return 0;

        case WM_CLOSE:
             DestroyWindow(hwnd);
            return 0;

        case WM_DESTROY:
            PostQuitMessage(0);
            return 0;

        default:
            return DefWindowProc(hwnd, message, wParam, lParam);
        }
}

int WINAPI WinMain(HINSTANCE cetteInstance, HINSTANCE precedenteInstance,
                                        LPSTR lignesDeCommande, int modeDAffichage)
{
       //Variables de la fonction principale
    MSG msg;
    WNDCLASS wc;
        HWND hwnd;
        inst = cetteInstance;
        // Structure de la classe de la fenêtre principale
    wc.style = 0 ;
    wc.lpfnWndProc = Procedure;
    wc.cbClsExtra = 0;
    wc.cbWndExtra = 0;
    wc.hInstance = cetteInstance;
    wc.hIcon = LoadIcon(NULL, IDI_APPLICATION);
    wc.hCursor = LoadCursor(NULL, IDC_ARROW);
    wc.hbrBackground =  (HBRUSH)(1+ COLOR_BTNFACE);
    wc.lpszMenuName =  NULL;
    wc.lpszClassName = "ClassePrincipale";

        //Enregistrer la classe de fenêtre
    if(!RegisterClass(&wc)) return FALSE;
    hwnd = CreateWindow("ClassePrincipale", "Wine menu organizer",WS_OVERLAPPEDWINDOW   ,
                              200,100,700,430, NULL, NULL, cetteInstance, NULL);
        if (!hwnd)  return FALSE;
    ShowWindow(hwnd,SW_SHOW);
        UpdateWindow( hwnd );

        //Boucle de message
    while (GetMessage(&msg, NULL, 0, 0))
    {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }
    return msg.wParam;
}
