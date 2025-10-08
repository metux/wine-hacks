1 cdecl UCNV_FROM_U_CALLBACK_ESCAPE(ptr ptr ptr long long long ptr) icu.UCNV_FROM_U_CALLBACK_ESCAPE
2 cdecl UCNV_FROM_U_CALLBACK_SKIP(ptr ptr ptr long long long ptr) icu.UCNV_FROM_U_CALLBACK_SKIP
3 cdecl UCNV_FROM_U_CALLBACK_STOP(ptr ptr ptr long long long ptr) icu.UCNV_FROM_U_CALLBACK_STOP
4 cdecl UCNV_FROM_U_CALLBACK_SUBSTITUTE(ptr ptr ptr long long long ptr) icu.UCNV_FROM_U_CALLBACK_SUBSTITUTE
5 cdecl UCNV_TO_U_CALLBACK_ESCAPE(ptr ptr str long long ptr) icu.UCNV_TO_U_CALLBACK_ESCAPE
6 cdecl UCNV_TO_U_CALLBACK_SKIP(ptr ptr str long long ptr) icu.UCNV_TO_U_CALLBACK_SKIP
7 cdecl UCNV_TO_U_CALLBACK_STOP(ptr ptr str long long ptr) icu.UCNV_TO_U_CALLBACK_STOP
8 cdecl UCNV_TO_U_CALLBACK_SUBSTITUTE(ptr ptr str long long ptr) icu.UCNV_TO_U_CALLBACK_SUBSTITUTE
9 cdecl u_UCharsToChars(ptr str long) icu.u_UCharsToChars
10 cdecl u_austrcpy(str ptr) icu.u_austrcpy
11 cdecl u_austrncpy(str ptr long) icu.u_austrncpy
12 cdecl u_catclose(long) icu.u_catclose
13 cdecl u_catgets(long long long ptr ptr ptr) icu.u_catgets
14 cdecl u_catopen(str str ptr) icu.u_catopen
15 cdecl u_charAge(long long) icu.u_charAge
16 cdecl u_charDigitValue(long) icu.u_charDigitValue
17 cdecl u_charDirection(long) icu.u_charDirection
18 cdecl u_charFromName(long str ptr) icu.u_charFromName
19 cdecl u_charMirror(long) icu.u_charMirror
20 cdecl u_charName(long long str long ptr) icu.u_charName
21 cdecl u_charType(long) icu.u_charType
22 cdecl u_charsToUChars(str ptr long) icu.u_charsToUChars
23 cdecl u_cleanup() icu.u_cleanup
24 cdecl u_countChar32(ptr long) icu.u_countChar32
25 cdecl u_digit(long long) icu.u_digit
26 cdecl u_enumCharNames(long long ptr ptr long ptr) icu.u_enumCharNames
27 cdecl u_enumCharTypes(ptr ptr) icu.u_enumCharTypes
28 cdecl u_errorName(long) icu.u_errorName
29 cdecl u_foldCase(long long) icu.u_foldCase
30 cdecl u_forDigit(long long) icu.u_forDigit
31 cdecl u_getBidiPairedBracket(long) icu.u_getBidiPairedBracket
32 cdecl u_getCombiningClass(long) icu.u_getCombiningClass
33 cdecl u_getDataVersion(long ptr) icu.u_getDataVersion
34 cdecl u_getFC_NFKC_Closure(long ptr long ptr) icu.u_getFC_NFKC_Closure
35 cdecl u_getIntPropertyMaxValue(long) icu.u_getIntPropertyMaxValue
36 cdecl u_getIntPropertyMinValue(long) icu.u_getIntPropertyMinValue
37 cdecl u_getIntPropertyValue(long long) icu.u_getIntPropertyValue
38 cdecl u_getNumericValue(long) icu.u_getNumericValue
39 cdecl u_getPropertyEnum(str) icu.u_getPropertyEnum
40 cdecl u_getPropertyName(long long) icu.u_getPropertyName
41 cdecl u_getPropertyValueEnum(long str) icu.u_getPropertyValueEnum
42 cdecl u_getPropertyValueName(long long long) icu.u_getPropertyValueName
43 cdecl u_getUnicodeVersion(long) icu.u_getUnicodeVersion
44 cdecl u_getVersion(long) icu.u_getVersion
45 cdecl u_hasBinaryProperty(long long) icu.u_hasBinaryProperty
46 cdecl u_init(ptr) icu.u_init
47 cdecl u_isIDIgnorable(long) icu.u_isIDIgnorable
48 cdecl u_isIDPart(long) icu.u_isIDPart
49 cdecl u_isIDStart(long) icu.u_isIDStart
50 cdecl u_isISOControl(long) icu.u_isISOControl
51 cdecl u_isJavaIDPart(long) icu.u_isJavaIDPart
52 cdecl u_isJavaIDStart(long) icu.u_isJavaIDStart
53 cdecl u_isJavaSpaceChar(long) icu.u_isJavaSpaceChar
54 cdecl u_isMirrored(long) icu.u_isMirrored
55 cdecl u_isUAlphabetic(long) icu.u_isUAlphabetic
56 cdecl u_isULowercase(long) icu.u_isULowercase
57 cdecl u_isUUppercase(long) icu.u_isUUppercase
58 cdecl u_isUWhiteSpace(long) icu.u_isUWhiteSpace
59 cdecl u_isWhitespace(long) icu.u_isWhitespace
60 cdecl u_isalnum(long) icu.u_isalnum
61 cdecl u_isalpha(long) icu.u_isalpha
62 cdecl u_isbase(long) icu.u_isbase
63 cdecl u_isblank(long) icu.u_isblank
64 cdecl u_iscntrl(long) icu.u_iscntrl
65 cdecl u_isdefined(long) icu.u_isdefined
66 cdecl u_isdigit(long) icu.u_isdigit
67 cdecl u_isgraph(long) icu.u_isgraph
68 cdecl u_islower(long) icu.u_islower
69 cdecl u_isprint(long) icu.u_isprint
70 cdecl u_ispunct(long) icu.u_ispunct
71 cdecl u_isspace(long) icu.u_isspace
72 cdecl u_istitle(long) icu.u_istitle
73 cdecl u_isupper(long) icu.u_isupper
74 cdecl u_isxdigit(long) icu.u_isxdigit
75 cdecl u_memcasecmp(ptr ptr long long) icu.u_memcasecmp
76 cdecl u_memchr(ptr long long) icu.u_memchr
77 cdecl u_memchr32(ptr long long) icu.u_memchr32
78 cdecl u_memcmp(ptr ptr long) icu.u_memcmp
79 cdecl u_memcmpCodePointOrder(ptr ptr long) icu.u_memcmpCodePointOrder
80 cdecl u_memcpy(ptr ptr long) icu.u_memcpy
81 cdecl u_memmove(ptr ptr long) icu.u_memmove
82 cdecl u_memrchr(ptr long long) icu.u_memrchr
83 cdecl u_memrchr32(ptr long long) icu.u_memrchr32
84 cdecl u_memset(ptr long long) icu.u_memset
85 cdecl u_setMemoryFunctions(ptr ptr ptr ptr ptr) icu.u_setMemoryFunctions
86 cdecl u_shapeArabic(ptr long ptr long long ptr) icu.u_shapeArabic
87 cdecl u_strCaseCompare(ptr long ptr long long ptr) icu.u_strCaseCompare
88 cdecl u_strCompare(ptr long ptr long long) icu.u_strCompare
89 cdecl u_strCompareIter(ptr ptr long) icu.u_strCompareIter
90 cdecl u_strFindFirst(ptr long ptr long) icu.u_strFindFirst
91 cdecl u_strFindLast(ptr long ptr long) icu.u_strFindLast
92 cdecl u_strFoldCase(ptr long ptr long long ptr) icu.u_strFoldCase
93 cdecl u_strFromJavaModifiedUTF8WithSub(ptr long ptr str long long ptr ptr) icu.u_strFromJavaModifiedUTF8WithSub
94 cdecl u_strFromUTF32(ptr long ptr ptr long ptr) icu.u_strFromUTF32
95 cdecl u_strFromUTF32WithSub(ptr long ptr ptr long long ptr ptr) icu.u_strFromUTF32WithSub
96 cdecl u_strFromUTF8(ptr long ptr str long ptr) icu.u_strFromUTF8
97 cdecl u_strFromUTF8Lenient(ptr long ptr str long ptr) icu.u_strFromUTF8Lenient
98 cdecl u_strFromUTF8WithSub(ptr long ptr str long long ptr ptr) icu.u_strFromUTF8WithSub
99 cdecl u_strFromWCS(ptr long ptr wstr long ptr) icu.u_strFromWCS
100 cdecl u_strHasMoreChar32Than(ptr long long) icu.u_strHasMoreChar32Than
101 cdecl u_strToJavaModifiedUTF8(str long ptr ptr long ptr) icu.u_strToJavaModifiedUTF8
102 cdecl u_strToLower(ptr long ptr long str ptr) icu.u_strToLower
103 cdecl u_strToTitle(ptr long ptr long ptr str ptr) icu.u_strToTitle
104 cdecl u_strToUTF32(ptr long ptr ptr long ptr) icu.u_strToUTF32
105 cdecl u_strToUTF32WithSub(ptr long ptr ptr long long ptr ptr) icu.u_strToUTF32WithSub
106 cdecl u_strToUTF8(str long ptr ptr long ptr) icu.u_strToUTF8
107 cdecl u_strToUTF8WithSub(str long ptr ptr long long ptr ptr) icu.u_strToUTF8WithSub
108 cdecl u_strToUpper(ptr long ptr long str ptr) icu.u_strToUpper
109 cdecl u_strToWCS(wstr long ptr ptr long ptr) icu.u_strToWCS
110 cdecl u_strcasecmp(ptr ptr long) icu.u_strcasecmp
111 cdecl u_strcat(ptr ptr) icu.u_strcat
112 cdecl u_strchr(ptr long) icu.u_strchr
113 cdecl u_strchr32(ptr long) icu.u_strchr32
114 cdecl u_strcmp(ptr ptr) icu.u_strcmp
115 cdecl u_strcmpCodePointOrder(ptr ptr) icu.u_strcmpCodePointOrder
116 cdecl u_strcpy(ptr ptr) icu.u_strcpy
117 cdecl u_strcspn(ptr ptr) icu.u_strcspn
118 cdecl u_strlen(ptr) icu.u_strlen
119 cdecl u_strncasecmp(ptr ptr long long) icu.u_strncasecmp
120 cdecl u_strncat(ptr ptr long) icu.u_strncat
121 cdecl u_strncmp(ptr ptr long) icu.u_strncmp
122 cdecl u_strncmpCodePointOrder(ptr ptr long) icu.u_strncmpCodePointOrder
123 cdecl u_strncpy(ptr ptr long) icu.u_strncpy
124 cdecl u_strpbrk(ptr ptr) icu.u_strpbrk
125 cdecl u_strrchr(ptr long) icu.u_strrchr
126 cdecl u_strrchr32(ptr long) icu.u_strrchr32
127 cdecl u_strrstr(ptr ptr) icu.u_strrstr
128 cdecl u_strspn(ptr ptr) icu.u_strspn
129 cdecl u_strstr(ptr ptr) icu.u_strstr
130 cdecl u_strtok_r(ptr ptr ptr) icu.u_strtok_r
131 cdecl u_tolower(long) icu.u_tolower
132 cdecl u_totitle(long) icu.u_totitle
133 cdecl u_toupper(long) icu.u_toupper
134 cdecl u_uastrcpy(ptr str) icu.u_uastrcpy
135 cdecl u_uastrncpy(ptr str long) icu.u_uastrncpy
136 cdecl u_unescape(str ptr long) icu.u_unescape
137 cdecl u_unescapeAt(long ptr long ptr) icu.u_unescapeAt
138 cdecl u_versionFromString(long str) icu.u_versionFromString
139 cdecl u_versionFromUString(long ptr) icu.u_versionFromUString
140 cdecl u_versionToString(long str) icu.u_versionToString
141 cdecl ubidi_close(ptr) icu.ubidi_close
142 cdecl ubidi_countParagraphs(ptr) icu.ubidi_countParagraphs
143 cdecl ubidi_countRuns(ptr ptr) icu.ubidi_countRuns
144 cdecl ubidi_getBaseDirection(ptr long) icu.ubidi_getBaseDirection
145 cdecl ubidi_getClassCallback(ptr ptr ptr) icu.ubidi_getClassCallback
146 cdecl ubidi_getCustomizedClass(ptr long) icu.ubidi_getCustomizedClass
147 cdecl ubidi_getDirection(ptr) icu.ubidi_getDirection
148 cdecl ubidi_getLength(ptr) icu.ubidi_getLength
149 cdecl ubidi_getLevelAt(ptr long) icu.ubidi_getLevelAt
150 cdecl ubidi_getLevels(ptr ptr) icu.ubidi_getLevels
151 cdecl ubidi_getLogicalIndex(ptr long ptr) icu.ubidi_getLogicalIndex
152 cdecl ubidi_getLogicalMap(ptr ptr ptr) icu.ubidi_getLogicalMap
153 cdecl ubidi_getLogicalRun(ptr long ptr ptr) icu.ubidi_getLogicalRun
154 cdecl ubidi_getParaLevel(ptr) icu.ubidi_getParaLevel
155 cdecl ubidi_getParagraph(ptr long ptr ptr ptr ptr) icu.ubidi_getParagraph
156 cdecl ubidi_getParagraphByIndex(ptr long ptr ptr ptr ptr) icu.ubidi_getParagraphByIndex
157 cdecl ubidi_getProcessedLength(ptr) icu.ubidi_getProcessedLength
158 cdecl ubidi_getReorderingMode(ptr) icu.ubidi_getReorderingMode
159 cdecl ubidi_getReorderingOptions(ptr) icu.ubidi_getReorderingOptions
160 cdecl ubidi_getResultLength(ptr) icu.ubidi_getResultLength
161 cdecl ubidi_getText(ptr) icu.ubidi_getText
162 cdecl ubidi_getVisualIndex(ptr long ptr) icu.ubidi_getVisualIndex
163 cdecl ubidi_getVisualMap(ptr ptr ptr) icu.ubidi_getVisualMap
164 cdecl ubidi_getVisualRun(ptr long ptr ptr) icu.ubidi_getVisualRun
165 cdecl ubidi_invertMap(ptr ptr long) icu.ubidi_invertMap
166 cdecl ubidi_isInverse(ptr) icu.ubidi_isInverse
167 cdecl ubidi_isOrderParagraphsLTR(ptr) icu.ubidi_isOrderParagraphsLTR
168 cdecl ubidi_open() icu.ubidi_open
169 cdecl ubidi_openSized(long long ptr) icu.ubidi_openSized
170 cdecl ubidi_orderParagraphsLTR(ptr long) icu.ubidi_orderParagraphsLTR
171 cdecl ubidi_reorderLogical(ptr long ptr) icu.ubidi_reorderLogical
172 cdecl ubidi_reorderVisual(ptr long ptr) icu.ubidi_reorderVisual
173 cdecl ubidi_setClassCallback(ptr ptr ptr ptr ptr ptr) icu.ubidi_setClassCallback
174 cdecl ubidi_setContext(ptr ptr long ptr long ptr) icu.ubidi_setContext
175 cdecl ubidi_setInverse(ptr long) icu.ubidi_setInverse
176 cdecl ubidi_setLine(ptr long long ptr ptr) icu.ubidi_setLine
177 cdecl ubidi_setPara(ptr ptr long long ptr ptr) icu.ubidi_setPara
178 cdecl ubidi_setReorderingMode(ptr long) icu.ubidi_setReorderingMode
179 cdecl ubidi_setReorderingOptions(ptr long) icu.ubidi_setReorderingOptions
180 cdecl ubidi_writeReordered(ptr ptr long long ptr) icu.ubidi_writeReordered
181 cdecl ubidi_writeReverse(ptr long ptr long long ptr) icu.ubidi_writeReverse
182 cdecl ubiditransform_close(ptr) icu.ubiditransform_close
183 cdecl ubiditransform_open(ptr) icu.ubiditransform_open
184 cdecl ubiditransform_transform(ptr ptr long ptr long long long long long long long ptr) icu.ubiditransform_transform
185 cdecl ublock_getCode(long) icu.ublock_getCode
186 cdecl ubrk_close(ptr) icu.ubrk_close
187 cdecl ubrk_countAvailable() icu.ubrk_countAvailable
188 cdecl ubrk_current(ptr) icu.ubrk_current
189 cdecl ubrk_first(ptr) icu.ubrk_first
190 cdecl ubrk_following(ptr long) icu.ubrk_following
191 cdecl ubrk_getAvailable(long) icu.ubrk_getAvailable
192 cdecl ubrk_getBinaryRules(ptr ptr long ptr) icu.ubrk_getBinaryRules
193 cdecl ubrk_getLocaleByType(ptr long ptr) icu.ubrk_getLocaleByType
194 cdecl ubrk_getRuleStatus(ptr) icu.ubrk_getRuleStatus
195 cdecl ubrk_getRuleStatusVec(ptr ptr long ptr) icu.ubrk_getRuleStatusVec
196 cdecl ubrk_isBoundary(ptr long) icu.ubrk_isBoundary
197 cdecl ubrk_last(ptr) icu.ubrk_last
198 cdecl ubrk_next(ptr) icu.ubrk_next
199 cdecl ubrk_open(long str ptr long ptr) icu.ubrk_open
200 cdecl ubrk_openBinaryRules(ptr long ptr long ptr) icu.ubrk_openBinaryRules
201 cdecl ubrk_openRules(ptr long ptr long ptr ptr) icu.ubrk_openRules
202 cdecl ubrk_preceding(ptr long) icu.ubrk_preceding
203 cdecl ubrk_previous(ptr) icu.ubrk_previous
204 cdecl ubrk_refreshUText(ptr ptr ptr) icu.ubrk_refreshUText
205 cdecl ubrk_safeClone(ptr ptr ptr ptr) icu.ubrk_safeClone
206 cdecl ubrk_setText(ptr ptr long ptr) icu.ubrk_setText
207 cdecl ubrk_setUText(ptr ptr ptr) icu.ubrk_setUText
208 cdecl ucasemap_close(ptr) icu.ucasemap_close
209 cdecl ucasemap_getBreakIterator(ptr) icu.ucasemap_getBreakIterator
210 cdecl ucasemap_getLocale(ptr) icu.ucasemap_getLocale
211 cdecl ucasemap_getOptions(ptr) icu.ucasemap_getOptions
212 cdecl ucasemap_open(str long ptr) icu.ucasemap_open
213 cdecl ucasemap_setBreakIterator(ptr ptr ptr) icu.ucasemap_setBreakIterator
214 cdecl ucasemap_setLocale(ptr str ptr) icu.ucasemap_setLocale
215 cdecl ucasemap_setOptions(ptr long ptr) icu.ucasemap_setOptions
216 cdecl ucasemap_toTitle(ptr ptr long ptr long ptr) icu.ucasemap_toTitle
217 cdecl ucasemap_utf8FoldCase(ptr str long str long ptr) icu.ucasemap_utf8FoldCase
218 cdecl ucasemap_utf8ToLower(ptr str long str long ptr) icu.ucasemap_utf8ToLower
219 cdecl ucasemap_utf8ToTitle(ptr str long str long ptr) icu.ucasemap_utf8ToTitle
220 cdecl ucasemap_utf8ToUpper(ptr str long str long ptr) icu.ucasemap_utf8ToUpper
221 cdecl ucnv_cbFromUWriteBytes(ptr str long long ptr) icu.ucnv_cbFromUWriteBytes
222 cdecl ucnv_cbFromUWriteSub(ptr long ptr) icu.ucnv_cbFromUWriteSub
223 cdecl ucnv_cbFromUWriteUChars(ptr ptr ptr long ptr) icu.ucnv_cbFromUWriteUChars
224 cdecl ucnv_cbToUWriteSub(ptr long ptr) icu.ucnv_cbToUWriteSub
225 cdecl ucnv_cbToUWriteUChars(ptr ptr long long ptr) icu.ucnv_cbToUWriteUChars
226 cdecl ucnv_close(ptr) icu.ucnv_close
227 cdecl ucnv_compareNames(str str) icu.ucnv_compareNames
228 cdecl ucnv_convert(str str str long str long ptr) icu.ucnv_convert
229 cdecl ucnv_convertEx(ptr ptr ptr str ptr str ptr ptr ptr ptr long long ptr) icu.ucnv_convertEx
230 cdecl ucnv_countAliases(str ptr) icu.ucnv_countAliases
231 cdecl ucnv_countAvailable() icu.ucnv_countAvailable
232 cdecl ucnv_countStandards() icu.ucnv_countStandards
233 cdecl ucnv_detectUnicodeSignature(str long ptr ptr) icu.ucnv_detectUnicodeSignature
234 cdecl ucnv_fixFileSeparator(ptr ptr long) icu.ucnv_fixFileSeparator
235 cdecl ucnv_flushCache() icu.ucnv_flushCache
236 cdecl ucnv_fromAlgorithmic(ptr long str long str long ptr) icu.ucnv_fromAlgorithmic
237 cdecl ucnv_fromUChars(ptr str long ptr long ptr) icu.ucnv_fromUChars
238 cdecl ucnv_fromUCountPending(ptr ptr) icu.ucnv_fromUCountPending
239 cdecl ucnv_fromUnicode(ptr ptr str ptr ptr ptr long ptr) icu.ucnv_fromUnicode
240 cdecl ucnv_getAlias(str long ptr) icu.ucnv_getAlias
241 cdecl ucnv_getAliases(str ptr ptr) icu.ucnv_getAliases
242 cdecl ucnv_getAvailableName(long) icu.ucnv_getAvailableName
243 cdecl ucnv_getCCSID(ptr ptr) icu.ucnv_getCCSID
244 cdecl ucnv_getCanonicalName(str str ptr) icu.ucnv_getCanonicalName
245 cdecl ucnv_getDefaultName() icu.ucnv_getDefaultName
246 cdecl ucnv_getDisplayName(ptr str ptr long ptr) icu.ucnv_getDisplayName
247 cdecl ucnv_getFromUCallBack(ptr ptr ptr) icu.ucnv_getFromUCallBack
248 cdecl ucnv_getInvalidChars(ptr str ptr ptr) icu.ucnv_getInvalidChars
249 cdecl ucnv_getInvalidUChars(ptr ptr ptr ptr) icu.ucnv_getInvalidUChars
250 cdecl ucnv_getMaxCharSize(ptr) icu.ucnv_getMaxCharSize
251 cdecl ucnv_getMinCharSize(ptr) icu.ucnv_getMinCharSize
252 cdecl ucnv_getName(ptr ptr) icu.ucnv_getName
253 cdecl ucnv_getNextUChar(ptr ptr str ptr) icu.ucnv_getNextUChar
254 cdecl ucnv_getPlatform(ptr ptr) icu.ucnv_getPlatform
255 cdecl ucnv_getStandard(long ptr) icu.ucnv_getStandard
256 cdecl ucnv_getStandardName(str str ptr) icu.ucnv_getStandardName
257 cdecl ucnv_getStarters(ptr long ptr) icu.ucnv_getStarters
258 cdecl ucnv_getSubstChars(ptr str ptr ptr) icu.ucnv_getSubstChars
259 cdecl ucnv_getToUCallBack(ptr ptr ptr) icu.ucnv_getToUCallBack
260 cdecl ucnv_getType(ptr) icu.ucnv_getType
261 cdecl ucnv_getUnicodeSet(ptr ptr long ptr) icu.ucnv_getUnicodeSet
262 cdecl ucnv_isAmbiguous(ptr) icu.ucnv_isAmbiguous
263 cdecl ucnv_isFixedWidth(ptr ptr) icu.ucnv_isFixedWidth
264 cdecl ucnv_open(str ptr) icu.ucnv_open
265 cdecl ucnv_openAllNames(ptr) icu.ucnv_openAllNames
266 cdecl ucnv_openCCSID(long long ptr) icu.ucnv_openCCSID
267 cdecl ucnv_openPackage(str str ptr) icu.ucnv_openPackage
268 cdecl ucnv_openStandardNames(str str ptr) icu.ucnv_openStandardNames
269 cdecl ucnv_openU(ptr ptr) icu.ucnv_openU
270 cdecl ucnv_reset(ptr) icu.ucnv_reset
271 cdecl ucnv_resetFromUnicode(ptr) icu.ucnv_resetFromUnicode
272 cdecl ucnv_resetToUnicode(ptr) icu.ucnv_resetToUnicode
273 cdecl ucnv_safeClone(ptr ptr ptr ptr) icu.ucnv_safeClone
274 cdecl ucnv_setDefaultName(str) icu.ucnv_setDefaultName
275 cdecl ucnv_setFallback(ptr long) icu.ucnv_setFallback
276 cdecl ucnv_setFromUCallBack(ptr long ptr ptr ptr ptr) icu.ucnv_setFromUCallBack
277 cdecl ucnv_setSubstChars(ptr str long ptr) icu.ucnv_setSubstChars
278 cdecl ucnv_setSubstString(ptr ptr long ptr) icu.ucnv_setSubstString
279 cdecl ucnv_setToUCallBack(ptr long ptr ptr ptr ptr) icu.ucnv_setToUCallBack
280 cdecl ucnv_toAlgorithmic(long ptr str long str long ptr) icu.ucnv_toAlgorithmic
281 cdecl ucnv_toUChars(ptr ptr long str long ptr) icu.ucnv_toUChars
282 cdecl ucnv_toUCountPending(ptr ptr) icu.ucnv_toUCountPending
283 cdecl ucnv_toUnicode(ptr ptr ptr ptr str ptr long ptr) icu.ucnv_toUnicode
284 cdecl ucnv_usesFallback(ptr) icu.ucnv_usesFallback
285 cdecl ucnvsel_close(ptr) icu.ucnvsel_close
286 cdecl ucnvsel_open(str long ptr long ptr) icu.ucnvsel_open
287 cdecl ucnvsel_openFromSerialized(ptr long ptr) icu.ucnvsel_openFromSerialized
288 cdecl ucnvsel_selectForString(ptr ptr long ptr) icu.ucnvsel_selectForString
289 cdecl ucnvsel_selectForUTF8(ptr str long ptr) icu.ucnvsel_selectForUTF8
290 cdecl ucnvsel_serialize(ptr ptr long ptr) icu.ucnvsel_serialize
291 cdecl ucurr_countCurrencies(str long ptr) icu.ucurr_countCurrencies
292 cdecl ucurr_forLocale(str ptr long ptr) icu.ucurr_forLocale
293 cdecl ucurr_forLocaleAndDate(str long long ptr long ptr) icu.ucurr_forLocaleAndDate
294 cdecl ucurr_getDefaultFractionDigits(ptr ptr) icu.ucurr_getDefaultFractionDigits
295 cdecl ucurr_getDefaultFractionDigitsForUsage(ptr long ptr) icu.ucurr_getDefaultFractionDigitsForUsage
296 cdecl ucurr_getKeywordValuesForLocale(str str long ptr) icu.ucurr_getKeywordValuesForLocale
297 cdecl ucurr_getName(ptr str long ptr ptr ptr) icu.ucurr_getName
298 cdecl ucurr_getNumericCode(ptr) icu.ucurr_getNumericCode
299 cdecl ucurr_getPluralName(ptr str ptr str ptr ptr) icu.ucurr_getPluralName
300 cdecl ucurr_getRoundingIncrement(ptr ptr) icu.ucurr_getRoundingIncrement
301 cdecl ucurr_getRoundingIncrementForUsage(ptr long ptr) icu.ucurr_getRoundingIncrementForUsage
302 cdecl ucurr_isAvailable(ptr long long ptr) icu.ucurr_isAvailable
303 cdecl ucurr_openISOCurrencies(long ptr) icu.ucurr_openISOCurrencies
304 cdecl ucurr_register(ptr str ptr) icu.ucurr_register
305 cdecl ucurr_unregister(long ptr) icu.ucurr_unregister
306 cdecl uenum_close(ptr) icu.uenum_close
307 cdecl uenum_count(ptr ptr) icu.uenum_count
308 cdecl uenum_next(ptr ptr ptr) icu.uenum_next
309 cdecl uenum_openCharStringsEnumeration(str long ptr) icu.uenum_openCharStringsEnumeration
310 cdecl uenum_openUCharStringsEnumeration(ptr long ptr) icu.uenum_openUCharStringsEnumeration
311 cdecl uenum_reset(ptr ptr) icu.uenum_reset
312 cdecl uenum_unext(ptr ptr ptr) icu.uenum_unext
313 cdecl uidna_close(ptr) icu.uidna_close
314 cdecl uidna_labelToASCII(ptr ptr long ptr long ptr ptr) icu.uidna_labelToASCII
315 cdecl uidna_labelToASCII_UTF8(ptr str long str long ptr ptr) icu.uidna_labelToASCII_UTF8
316 cdecl uidna_labelToUnicode(ptr ptr long ptr long ptr ptr) icu.uidna_labelToUnicode
317 cdecl uidna_labelToUnicodeUTF8(ptr str long str long ptr ptr) icu.uidna_labelToUnicodeUTF8
318 cdecl uidna_nameToASCII(ptr ptr long ptr long ptr ptr) icu.uidna_nameToASCII
319 cdecl uidna_nameToASCII_UTF8(ptr str long str long ptr ptr) icu.uidna_nameToASCII_UTF8
320 cdecl uidna_nameToUnicode(ptr ptr long ptr long ptr ptr) icu.uidna_nameToUnicode
321 cdecl uidna_nameToUnicodeUTF8(ptr str long str long ptr ptr) icu.uidna_nameToUnicodeUTF8
322 cdecl uidna_openUTS46(long ptr) icu.uidna_openUTS46
323 cdecl uiter_current32(ptr) icu.uiter_current32
324 cdecl uiter_getState(ptr) icu.uiter_getState
325 cdecl uiter_next32(ptr) icu.uiter_next32
326 cdecl uiter_previous32(ptr) icu.uiter_previous32
327 cdecl uiter_setState(ptr long ptr) icu.uiter_setState
328 cdecl uiter_setString(ptr ptr long) icu.uiter_setString
329 cdecl uiter_setUTF16BE(ptr str long) icu.uiter_setUTF16BE
330 cdecl uiter_setUTF8(ptr str long) icu.uiter_setUTF8
331 cdecl uldn_close(ptr) icu.uldn_close
332 cdecl uldn_getContext(ptr long ptr) icu.uldn_getContext
333 cdecl uldn_getDialectHandling(ptr) icu.uldn_getDialectHandling
334 cdecl uldn_getLocale(ptr) icu.uldn_getLocale
335 cdecl uldn_keyDisplayName(ptr str ptr long ptr) icu.uldn_keyDisplayName
336 cdecl uldn_keyValueDisplayName(ptr str str ptr long ptr) icu.uldn_keyValueDisplayName
337 cdecl uldn_languageDisplayName(ptr str ptr long ptr) icu.uldn_languageDisplayName
338 cdecl uldn_localeDisplayName(ptr str ptr long ptr) icu.uldn_localeDisplayName
339 cdecl uldn_open(str long ptr) icu.uldn_open
340 cdecl uldn_openForContext(str ptr long ptr) icu.uldn_openForContext
341 cdecl uldn_regionDisplayName(ptr str ptr long ptr) icu.uldn_regionDisplayName
342 cdecl uldn_scriptCodeDisplayName(ptr long ptr long ptr) icu.uldn_scriptCodeDisplayName
343 cdecl uldn_scriptDisplayName(ptr str ptr long ptr) icu.uldn_scriptDisplayName
344 cdecl uldn_variantDisplayName(ptr str ptr long ptr) icu.uldn_variantDisplayName
345 cdecl ulistfmt_close(ptr) icu.ulistfmt_close
346 cdecl ulistfmt_format(ptr ptr ptr long ptr long ptr) icu.ulistfmt_format
347 cdecl ulistfmt_open(str ptr) icu.ulistfmt_open
348 cdecl uloc_acceptLanguage(str long ptr ptr long ptr ptr) icu.uloc_acceptLanguage
349 cdecl uloc_acceptLanguageFromHTTP(str long ptr str ptr ptr) icu.uloc_acceptLanguageFromHTTP
350 cdecl uloc_addLikelySubtags(str str long ptr) icu.uloc_addLikelySubtags
351 cdecl uloc_canonicalize(str str long ptr) icu.uloc_canonicalize
352 cdecl uloc_countAvailable() icu.uloc_countAvailable
353 cdecl uloc_forLanguageTag(str str long ptr ptr) icu.uloc_forLanguageTag
354 cdecl uloc_getAvailable(long) icu.uloc_getAvailable
355 cdecl uloc_getBaseName(str str long ptr) icu.uloc_getBaseName
356 cdecl uloc_getCharacterOrientation(str ptr) icu.uloc_getCharacterOrientation
357 cdecl uloc_getCountry(str str long ptr) icu.uloc_getCountry
358 cdecl uloc_getDefault() icu.uloc_getDefault
359 cdecl uloc_getDisplayCountry(str str ptr long ptr) icu.uloc_getDisplayCountry
360 cdecl uloc_getDisplayKeyword(str str ptr long ptr) icu.uloc_getDisplayKeyword
361 cdecl uloc_getDisplayKeywordValue(str str str ptr long ptr) icu.uloc_getDisplayKeywordValue
362 cdecl uloc_getDisplayLanguage(str str ptr long ptr) icu.uloc_getDisplayLanguage
363 cdecl uloc_getDisplayName(str str ptr long ptr) icu.uloc_getDisplayName
364 cdecl uloc_getDisplayScript(str str ptr long ptr) icu.uloc_getDisplayScript
365 cdecl uloc_getDisplayVariant(str str ptr long ptr) icu.uloc_getDisplayVariant
366 cdecl uloc_getISO3Country(str) icu.uloc_getISO3Country
367 cdecl uloc_getISO3Language(str) icu.uloc_getISO3Language
368 cdecl uloc_getISOCountries() icu.uloc_getISOCountries
369 cdecl uloc_getISOLanguages() icu.uloc_getISOLanguages
370 cdecl uloc_getKeywordValue(str str str long ptr) icu.uloc_getKeywordValue
371 cdecl uloc_getLCID(str) icu.uloc_getLCID
372 cdecl uloc_getLanguage(str str long ptr) icu.uloc_getLanguage
373 cdecl uloc_getLineOrientation(str ptr) icu.uloc_getLineOrientation
374 cdecl uloc_getLocaleForLCID(long str long ptr) icu.uloc_getLocaleForLCID
375 cdecl uloc_getName(str str long ptr) icu.uloc_getName
376 cdecl uloc_getParent(str str long ptr) icu.uloc_getParent
377 cdecl uloc_getScript(str str long ptr) icu.uloc_getScript
378 cdecl uloc_getVariant(str str long ptr) icu.uloc_getVariant
379 cdecl uloc_isRightToLeft(str) icu.uloc_isRightToLeft
380 cdecl uloc_minimizeSubtags(str str long ptr) icu.uloc_minimizeSubtags
381 cdecl uloc_openKeywords(str ptr) icu.uloc_openKeywords
382 cdecl uloc_setDefault(str ptr) icu.uloc_setDefault
383 cdecl uloc_setKeywordValue(str str str long ptr) icu.uloc_setKeywordValue
384 cdecl uloc_toLanguageTag(str str long long ptr) icu.uloc_toLanguageTag
385 cdecl uloc_toLegacyKey(str) icu.uloc_toLegacyKey
386 cdecl uloc_toLegacyType(str str) icu.uloc_toLegacyType
387 cdecl uloc_toUnicodeLocaleKey(str) icu.uloc_toUnicodeLocaleKey
388 cdecl uloc_toUnicodeLocaleType(str str) icu.uloc_toUnicodeLocaleType
389 cdecl unorm2_append(ptr ptr long long ptr long ptr) icu.unorm2_append
390 cdecl unorm2_close(ptr) icu.unorm2_close
391 cdecl unorm2_composePair(ptr long long) icu.unorm2_composePair
392 cdecl unorm2_getCombiningClass(ptr long) icu.unorm2_getCombiningClass
393 cdecl unorm2_getDecomposition(ptr long ptr long ptr) icu.unorm2_getDecomposition
394 cdecl unorm2_getInstance(str str long ptr) icu.unorm2_getInstance
395 cdecl unorm2_getNFCInstance(ptr) icu.unorm2_getNFCInstance
396 cdecl unorm2_getNFDInstance(ptr) icu.unorm2_getNFDInstance
397 cdecl unorm2_getNFKCCasefoldInstance(ptr) icu.unorm2_getNFKCCasefoldInstance
398 cdecl unorm2_getNFKCInstance(ptr) icu.unorm2_getNFKCInstance
399 cdecl unorm2_getNFKDInstance(ptr) icu.unorm2_getNFKDInstance
400 cdecl unorm2_getRawDecomposition(ptr long ptr long ptr) icu.unorm2_getRawDecomposition
401 cdecl unorm2_hasBoundaryAfter(ptr long) icu.unorm2_hasBoundaryAfter
402 cdecl unorm2_hasBoundaryBefore(ptr long) icu.unorm2_hasBoundaryBefore
403 cdecl unorm2_isInert(ptr long) icu.unorm2_isInert
404 cdecl unorm2_isNormalized(ptr ptr long ptr) icu.unorm2_isNormalized
405 cdecl unorm2_normalize(ptr ptr long ptr long ptr) icu.unorm2_normalize
406 cdecl unorm2_normalizeSecondAndAppend(ptr ptr long long ptr long ptr) icu.unorm2_normalizeSecondAndAppend
407 cdecl unorm2_openFiltered(ptr ptr ptr) icu.unorm2_openFiltered
408 cdecl unorm2_quickCheck(ptr ptr long ptr) icu.unorm2_quickCheck
409 cdecl unorm2_spanQuickCheckYes(ptr ptr long ptr) icu.unorm2_spanQuickCheckYes
410 cdecl unorm_compare(ptr long ptr long long ptr) icu.unorm_compare
411 cdecl ures_close(ptr) icu.ures_close
412 cdecl ures_getBinary(ptr ptr ptr) icu.ures_getBinary
413 cdecl ures_getByIndex(ptr long ptr ptr) icu.ures_getByIndex
414 cdecl ures_getByKey(ptr str ptr ptr) icu.ures_getByKey
415 cdecl ures_getInt(ptr ptr) icu.ures_getInt
416 cdecl ures_getIntVector(ptr ptr ptr) icu.ures_getIntVector
417 cdecl ures_getKey(ptr) icu.ures_getKey
418 cdecl ures_getLocaleByType(ptr long ptr) icu.ures_getLocaleByType
419 cdecl ures_getNextResource(ptr ptr ptr) icu.ures_getNextResource
420 cdecl ures_getNextString(ptr ptr ptr ptr) icu.ures_getNextString
421 cdecl ures_getSize(ptr) icu.ures_getSize
422 cdecl ures_getString(ptr ptr ptr) icu.ures_getString
423 cdecl ures_getStringByIndex(ptr long ptr ptr) icu.ures_getStringByIndex
424 cdecl ures_getStringByKey(ptr str ptr ptr) icu.ures_getStringByKey
425 cdecl ures_getType(ptr) icu.ures_getType
426 cdecl ures_getUInt(ptr ptr) icu.ures_getUInt
427 cdecl ures_getUTF8String(ptr str ptr long ptr) icu.ures_getUTF8String
428 cdecl ures_getUTF8StringByIndex(ptr long str ptr long ptr) icu.ures_getUTF8StringByIndex
429 cdecl ures_getUTF8StringByKey(ptr str str ptr long ptr) icu.ures_getUTF8StringByKey
430 cdecl ures_getVersion(ptr long) icu.ures_getVersion
431 cdecl ures_hasNext(ptr) icu.ures_hasNext
432 cdecl ures_open(str str ptr) icu.ures_open
433 cdecl ures_openAvailableLocales(str ptr) icu.ures_openAvailableLocales
434 cdecl ures_openDirect(str str ptr) icu.ures_openDirect
435 cdecl ures_openU(ptr str ptr) icu.ures_openU
436 cdecl ures_resetIterator(ptr) icu.ures_resetIterator
437 cdecl uscript_breaksBetweenLetters(long) icu.uscript_breaksBetweenLetters
438 cdecl uscript_getCode(str ptr long ptr) icu.uscript_getCode
439 cdecl uscript_getName(long) icu.uscript_getName
440 cdecl uscript_getSampleString(long ptr long ptr) icu.uscript_getSampleString
441 cdecl uscript_getScript(long ptr) icu.uscript_getScript
442 cdecl uscript_getScriptExtensions(long ptr long ptr) icu.uscript_getScriptExtensions
443 cdecl uscript_getShortName(long) icu.uscript_getShortName
444 cdecl uscript_getUsage(long) icu.uscript_getUsage
445 cdecl uscript_hasScript(long long) icu.uscript_hasScript
446 cdecl uscript_isCased(long) icu.uscript_isCased
447 cdecl uscript_isRightToLeft(long) icu.uscript_isRightToLeft
448 cdecl uset_add(ptr long) icu.uset_add
449 cdecl uset_addAll(ptr ptr) icu.uset_addAll
450 cdecl uset_addAllCodePoints(ptr ptr long) icu.uset_addAllCodePoints
451 cdecl uset_addRange(ptr long long) icu.uset_addRange
452 cdecl uset_addString(ptr ptr long) icu.uset_addString
453 cdecl uset_applyIntPropertyValue(ptr long long ptr) icu.uset_applyIntPropertyValue
454 cdecl uset_applyPattern(ptr ptr long long ptr) icu.uset_applyPattern
455 cdecl uset_applyPropertyAlias(ptr ptr long ptr long ptr) icu.uset_applyPropertyAlias
456 cdecl uset_charAt(ptr long) icu.uset_charAt
457 cdecl uset_clear(ptr) icu.uset_clear
458 cdecl uset_clone(ptr) icu.uset_clone
459 cdecl uset_cloneAsThawed(ptr) icu.uset_cloneAsThawed
460 cdecl uset_close(ptr) icu.uset_close
461 cdecl uset_closeOver(ptr long) icu.uset_closeOver
462 cdecl uset_compact(ptr) icu.uset_compact
463 cdecl uset_complement(ptr) icu.uset_complement
464 cdecl uset_complementAll(ptr ptr) icu.uset_complementAll
465 cdecl uset_contains(ptr long) icu.uset_contains
466 cdecl uset_containsAll(ptr ptr) icu.uset_containsAll
467 cdecl uset_containsAllCodePoints(ptr ptr long) icu.uset_containsAllCodePoints
468 cdecl uset_containsNone(ptr ptr) icu.uset_containsNone
469 cdecl uset_containsRange(ptr long long) icu.uset_containsRange
470 cdecl uset_containsSome(ptr ptr) icu.uset_containsSome
471 cdecl uset_containsString(ptr ptr long) icu.uset_containsString
472 cdecl uset_equals(ptr ptr) icu.uset_equals
473 cdecl uset_freeze(ptr) icu.uset_freeze
474 cdecl uset_getItem(ptr long ptr ptr ptr long ptr) icu.uset_getItem
475 cdecl uset_getItemCount(ptr) icu.uset_getItemCount
476 cdecl uset_getSerializedRange(ptr long ptr ptr) icu.uset_getSerializedRange
477 cdecl uset_getSerializedRangeCount(ptr) icu.uset_getSerializedRangeCount
478 cdecl uset_getSerializedSet(ptr ptr long) icu.uset_getSerializedSet
479 cdecl uset_indexOf(ptr long) icu.uset_indexOf
480 cdecl uset_isEmpty(ptr) icu.uset_isEmpty
481 cdecl uset_isFrozen(ptr) icu.uset_isFrozen
482 cdecl uset_open(long long) icu.uset_open
483 cdecl uset_openEmpty() icu.uset_openEmpty
484 cdecl uset_openPattern(ptr long ptr) icu.uset_openPattern
485 cdecl uset_openPatternOptions(ptr long long ptr) icu.uset_openPatternOptions
486 cdecl uset_remove(ptr long) icu.uset_remove
487 cdecl uset_removeAll(ptr ptr) icu.uset_removeAll
488 cdecl uset_removeAllStrings(ptr) icu.uset_removeAllStrings
489 cdecl uset_removeRange(ptr long long) icu.uset_removeRange
490 cdecl uset_removeString(ptr ptr long) icu.uset_removeString
491 cdecl uset_resemblesPattern(ptr long long) icu.uset_resemblesPattern
492 cdecl uset_retain(ptr long long) icu.uset_retain
493 cdecl uset_retainAll(ptr ptr) icu.uset_retainAll
494 cdecl uset_serialize(ptr ptr long ptr) icu.uset_serialize
495 cdecl uset_serializedContains(ptr long) icu.uset_serializedContains
496 cdecl uset_set(ptr long long) icu.uset_set
497 cdecl uset_setSerializedToOne(ptr long) icu.uset_setSerializedToOne
498 cdecl uset_size(ptr) icu.uset_size
499 cdecl uset_span(ptr ptr long long) icu.uset_span
500 cdecl uset_spanBack(ptr ptr long long) icu.uset_spanBack
501 cdecl uset_spanBackUTF8(ptr str long long) icu.uset_spanBackUTF8
502 cdecl uset_spanUTF8(ptr str long long) icu.uset_spanUTF8
503 cdecl uset_toPattern(ptr ptr long long ptr) icu.uset_toPattern
504 cdecl usprep_close(ptr) icu.usprep_close
505 cdecl usprep_open(str str ptr) icu.usprep_open
506 cdecl usprep_openByType(long ptr) icu.usprep_openByType
507 cdecl usprep_prepare(ptr ptr long ptr long long ptr ptr) icu.usprep_prepare
508 cdecl utext_char32At(ptr long) icu.utext_char32At
509 cdecl utext_clone(ptr ptr long long ptr) icu.utext_clone
510 cdecl utext_close(ptr) icu.utext_close
511 cdecl utext_copy(ptr long long long long ptr) icu.utext_copy
512 cdecl utext_current32(ptr) icu.utext_current32
513 cdecl utext_equals(ptr ptr) icu.utext_equals
514 cdecl utext_extract(ptr long long ptr long ptr) icu.utext_extract
515 cdecl utext_freeze(ptr) icu.utext_freeze
516 cdecl utext_getNativeIndex(ptr) icu.utext_getNativeIndex
517 cdecl utext_getPreviousNativeIndex(ptr) icu.utext_getPreviousNativeIndex
518 cdecl utext_hasMetaData(ptr) icu.utext_hasMetaData
519 cdecl utext_isLengthExpensive(ptr) icu.utext_isLengthExpensive
520 cdecl utext_isWritable(ptr) icu.utext_isWritable
521 cdecl utext_moveIndex32(ptr long) icu.utext_moveIndex32
522 cdecl utext_nativeLength(ptr) icu.utext_nativeLength
523 cdecl utext_next32(ptr) icu.utext_next32
524 cdecl utext_next32From(ptr long) icu.utext_next32From
525 cdecl utext_openUChars(ptr ptr long ptr) icu.utext_openUChars
526 cdecl utext_openUTF8(ptr str long ptr) icu.utext_openUTF8
527 cdecl utext_previous32(ptr) icu.utext_previous32
528 cdecl utext_previous32From(ptr long) icu.utext_previous32From
529 cdecl utext_replace(ptr long long ptr long ptr) icu.utext_replace
530 cdecl utext_setNativeIndex(ptr long) icu.utext_setNativeIndex
531 cdecl utext_setup(ptr long ptr) icu.utext_setup
532 cdecl utf8_appendCharSafeBody(ptr long long long ptr) icu.utf8_appendCharSafeBody
533 cdecl utf8_back1SafeBody(ptr long long) icu.utf8_back1SafeBody
534 cdecl utf8_nextCharSafeBody(ptr ptr long long long) icu.utf8_nextCharSafeBody
535 cdecl utf8_prevCharSafeBody(ptr long ptr long long) icu.utf8_prevCharSafeBody
536 varargs utrace_format(str long long str) icu.utrace_format
537 cdecl utrace_functionName(long) icu.utrace_functionName
538 cdecl utrace_getFunctions(ptr ptr ptr ptr) icu.utrace_getFunctions
539 cdecl utrace_getLevel() icu.utrace_getLevel
540 cdecl utrace_setFunctions(ptr ptr ptr ptr) icu.utrace_setFunctions
541 cdecl utrace_setLevel(long) icu.utrace_setLevel
542 cdecl utrace_vformat(str long long str long) icu.utrace_vformat
