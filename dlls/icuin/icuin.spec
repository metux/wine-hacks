1 varargs u_formatMessage(str ptr long ptr long ptr) icu.u_formatMessage
2 varargs u_formatMessageWithError(str ptr long ptr long ptr ptr) icu.u_formatMessageWithError
3 varargs u_parseMessage(str ptr long ptr long ptr) icu.u_parseMessage
4 varargs u_parseMessageWithError(str ptr long ptr long ptr ptr) icu.u_parseMessageWithError
5 cdecl u_vformatMessage(str ptr long ptr long long ptr) icu.u_vformatMessage
6 cdecl u_vformatMessageWithError(str ptr long ptr long ptr long ptr) icu.u_vformatMessageWithError
7 cdecl u_vparseMessage(str ptr long ptr long long ptr) icu.u_vparseMessage
8 cdecl u_vparseMessageWithError(str ptr long ptr long long ptr ptr) icu.u_vparseMessageWithError
9 cdecl ucal_add(ptr long long ptr) icu.ucal_add
10 cdecl ucal_clear(ptr) icu.ucal_clear
11 cdecl ucal_clearField(ptr long) icu.ucal_clearField
12 cdecl ucal_clone(ptr ptr) icu.ucal_clone
13 cdecl ucal_close(ptr) icu.ucal_close
14 cdecl ucal_countAvailable() icu.ucal_countAvailable
15 cdecl ucal_equivalentTo(ptr ptr) icu.ucal_equivalentTo
16 cdecl ucal_get(ptr long ptr) icu.ucal_get
17 cdecl ucal_getAttribute(ptr long) icu.ucal_getAttribute
18 cdecl ucal_getAvailable(long) icu.ucal_getAvailable
19 cdecl ucal_getCanonicalTimeZoneID(ptr long ptr long ptr ptr) icu.ucal_getCanonicalTimeZoneID
20 cdecl ucal_getDSTSavings(ptr ptr) icu.ucal_getDSTSavings
21 cdecl ucal_getDayOfWeekType(ptr long ptr) icu.ucal_getDayOfWeekType
22 cdecl ucal_getDefaultTimeZone(ptr long ptr) icu.ucal_getDefaultTimeZone
23 cdecl ucal_getFieldDifference(ptr long long ptr) icu.ucal_getFieldDifference
24 cdecl ucal_getGregorianChange(ptr ptr) icu.ucal_getGregorianChange
25 cdecl ucal_getKeywordValuesForLocale(str str long ptr) icu.ucal_getKeywordValuesForLocale
26 cdecl ucal_getLimit(ptr long long ptr) icu.ucal_getLimit
27 cdecl ucal_getLocaleByType(ptr long ptr) icu.ucal_getLocaleByType
28 cdecl ucal_getMillis(ptr ptr) icu.ucal_getMillis
29 cdecl ucal_getNow() icu.ucal_getNow
30 cdecl ucal_getTZDataVersion(ptr) icu.ucal_getTZDataVersion
31 cdecl ucal_getTimeZoneDisplayName(ptr long str ptr long ptr) icu.ucal_getTimeZoneDisplayName
32 cdecl ucal_getTimeZoneID(ptr ptr long ptr) icu.ucal_getTimeZoneID
33 cdecl ucal_getTimeZoneIDForWindowsID(ptr long str ptr long ptr) icu.ucal_getTimeZoneIDForWindowsID
34 cdecl ucal_getTimeZoneTransitionDate(ptr long ptr ptr) icu.ucal_getTimeZoneTransitionDate
35 cdecl ucal_getType(ptr ptr) icu.ucal_getType
36 cdecl ucal_getWeekendTransition(ptr long ptr) icu.ucal_getWeekendTransition
37 cdecl ucal_getWindowsTimeZoneID(ptr long ptr long ptr) icu.ucal_getWindowsTimeZoneID
38 cdecl ucal_inDaylightTime(ptr ptr) icu.ucal_inDaylightTime
39 cdecl ucal_isSet(ptr long) icu.ucal_isSet
40 cdecl ucal_isWeekend(ptr long ptr) icu.ucal_isWeekend
41 cdecl ucal_open(ptr long str long ptr) icu.ucal_open
42 cdecl ucal_openCountryTimeZones(str ptr) icu.ucal_openCountryTimeZones
43 cdecl ucal_openTimeZoneIDEnumeration(long str ptr ptr) icu.ucal_openTimeZoneIDEnumeration
44 cdecl ucal_openTimeZones(ptr) icu.ucal_openTimeZones
45 cdecl ucal_roll(ptr long long ptr) icu.ucal_roll
46 cdecl ucal_set(ptr long long) icu.ucal_set
47 cdecl ucal_setAttribute(ptr long long) icu.ucal_setAttribute
48 cdecl ucal_setDate(ptr long long long ptr) icu.ucal_setDate
49 cdecl ucal_setDateTime(ptr long long long long long long ptr) icu.ucal_setDateTime
50 cdecl ucal_setDefaultTimeZone(ptr ptr) icu.ucal_setDefaultTimeZone
51 cdecl ucal_setGregorianChange(ptr long ptr) icu.ucal_setGregorianChange
52 cdecl ucal_setMillis(ptr long ptr) icu.ucal_setMillis
53 cdecl ucal_setTimeZone(ptr ptr long ptr) icu.ucal_setTimeZone
54 cdecl ucol_cloneBinary(ptr ptr long ptr) icu.ucol_cloneBinary
55 cdecl ucol_close(ptr) icu.ucol_close
56 cdecl ucol_closeElements(ptr) icu.ucol_closeElements
57 cdecl ucol_countAvailable() icu.ucol_countAvailable
58 cdecl ucol_equal(ptr ptr long ptr long) icu.ucol_equal
59 cdecl ucol_getAttribute(ptr long ptr) icu.ucol_getAttribute
60 cdecl ucol_getAvailable(long) icu.ucol_getAvailable
61 cdecl ucol_getBound(ptr long long long ptr long ptr) icu.ucol_getBound
62 cdecl ucol_getContractionsAndExpansions(ptr ptr ptr long ptr) icu.ucol_getContractionsAndExpansions
63 cdecl ucol_getDisplayName(str str ptr long ptr) icu.ucol_getDisplayName
64 cdecl ucol_getEquivalentReorderCodes(long ptr long ptr) icu.ucol_getEquivalentReorderCodes
65 cdecl ucol_getFunctionalEquivalent(str long str str ptr ptr) icu.ucol_getFunctionalEquivalent
66 cdecl ucol_getKeywordValues(str ptr) icu.ucol_getKeywordValues
67 cdecl ucol_getKeywordValuesForLocale(str str long ptr) icu.ucol_getKeywordValuesForLocale
68 cdecl ucol_getKeywords(ptr) icu.ucol_getKeywords
69 cdecl ucol_getLocaleByType(ptr long ptr) icu.ucol_getLocaleByType
70 cdecl ucol_getMaxExpansion(ptr long) icu.ucol_getMaxExpansion
71 cdecl ucol_getMaxVariable(ptr) icu.ucol_getMaxVariable
72 cdecl ucol_getOffset(ptr) icu.ucol_getOffset
73 cdecl ucol_getReorderCodes(ptr ptr long ptr) icu.ucol_getReorderCodes
74 cdecl ucol_getRules(ptr ptr) icu.ucol_getRules
75 cdecl ucol_getRulesEx(ptr long ptr long) icu.ucol_getRulesEx
76 cdecl ucol_getSortKey(ptr ptr long ptr long) icu.ucol_getSortKey
77 cdecl ucol_getStrength(ptr) icu.ucol_getStrength
78 cdecl ucol_getTailoredSet(ptr ptr) icu.ucol_getTailoredSet
79 cdecl ucol_getUCAVersion(ptr long) icu.ucol_getUCAVersion
80 cdecl ucol_getVariableTop(ptr ptr) icu.ucol_getVariableTop
81 cdecl ucol_getVersion(ptr long) icu.ucol_getVersion
82 cdecl ucol_greater(ptr ptr long ptr long) icu.ucol_greater
83 cdecl ucol_greaterOrEqual(ptr ptr long ptr long) icu.ucol_greaterOrEqual
84 cdecl ucol_keyHashCode(ptr long) icu.ucol_keyHashCode
85 cdecl ucol_mergeSortkeys(ptr long ptr long ptr long) icu.ucol_mergeSortkeys
86 cdecl ucol_next(ptr ptr) icu.ucol_next
87 cdecl ucol_nextSortKeyPart(ptr ptr long ptr long ptr) icu.ucol_nextSortKeyPart
88 cdecl ucol_open(str ptr) icu.ucol_open
89 cdecl ucol_openAvailableLocales(ptr) icu.ucol_openAvailableLocales
90 cdecl ucol_openBinary(ptr long ptr ptr) icu.ucol_openBinary
91 cdecl ucol_openElements(ptr ptr long ptr) icu.ucol_openElements
92 cdecl ucol_openRules(ptr long long long ptr ptr) icu.ucol_openRules
93 cdecl ucol_previous(ptr ptr) icu.ucol_previous
94 cdecl ucol_primaryOrder(long) icu.ucol_primaryOrder
95 cdecl ucol_reset(ptr) icu.ucol_reset
96 cdecl ucol_safeClone(ptr ptr ptr ptr) icu.ucol_safeClone
97 cdecl ucol_secondaryOrder(long) icu.ucol_secondaryOrder
98 cdecl ucol_setAttribute(ptr long long ptr) icu.ucol_setAttribute
99 cdecl ucol_setMaxVariable(ptr long ptr) icu.ucol_setMaxVariable
100 cdecl ucol_setOffset(ptr long ptr) icu.ucol_setOffset
101 cdecl ucol_setReorderCodes(ptr ptr long ptr) icu.ucol_setReorderCodes
102 cdecl ucol_setStrength(ptr long) icu.ucol_setStrength
103 cdecl ucol_setText(ptr ptr long ptr) icu.ucol_setText
104 cdecl ucol_strcoll(ptr ptr long ptr long) icu.ucol_strcoll
105 cdecl ucol_strcollIter(ptr ptr ptr ptr) icu.ucol_strcollIter
106 cdecl ucol_strcollUTF8(ptr str long str long ptr) icu.ucol_strcollUTF8
107 cdecl ucol_tertiaryOrder(long) icu.ucol_tertiaryOrder
108 cdecl ucsdet_close(ptr) icu.ucsdet_close
109 cdecl ucsdet_detect(ptr ptr) icu.ucsdet_detect
110 cdecl ucsdet_detectAll(ptr ptr ptr) icu.ucsdet_detectAll
111 cdecl ucsdet_enableInputFilter(ptr long) icu.ucsdet_enableInputFilter
112 cdecl ucsdet_getAllDetectableCharsets(ptr ptr) icu.ucsdet_getAllDetectableCharsets
113 cdecl ucsdet_getConfidence(ptr ptr) icu.ucsdet_getConfidence
114 cdecl ucsdet_getLanguage(ptr ptr) icu.ucsdet_getLanguage
115 cdecl ucsdet_getName(ptr ptr) icu.ucsdet_getName
116 cdecl ucsdet_getUChars(ptr ptr long ptr) icu.ucsdet_getUChars
117 cdecl ucsdet_isInputFilterEnabled(ptr) icu.ucsdet_isInputFilterEnabled
118 cdecl ucsdet_open(ptr) icu.ucsdet_open
119 cdecl ucsdet_setDeclaredEncoding(ptr str long ptr) icu.ucsdet_setDeclaredEncoding
120 cdecl ucsdet_setText(ptr str long ptr) icu.ucsdet_setText
121 cdecl udat_adoptNumberFormat(ptr ptr) icu.udat_adoptNumberFormat
122 cdecl udat_adoptNumberFormatForFields(ptr ptr ptr ptr) icu.udat_adoptNumberFormatForFields
123 cdecl udat_applyPattern(ptr long ptr long) icu.udat_applyPattern
124 cdecl udat_clone(ptr ptr) icu.udat_clone
125 cdecl udat_close(ptr) icu.udat_close
126 cdecl udat_countAvailable() icu.udat_countAvailable
127 cdecl udat_countSymbols(ptr long) icu.udat_countSymbols
128 cdecl udat_format(ptr long ptr long ptr ptr) icu.udat_format
129 cdecl udat_formatCalendar(ptr ptr ptr long ptr ptr) icu.udat_formatCalendar
130 cdecl udat_formatCalendarForFields(ptr ptr ptr long ptr ptr) icu.udat_formatCalendarForFields
131 cdecl udat_formatForFields(ptr long ptr long ptr ptr) icu.udat_formatForFields
132 cdecl udat_get2DigitYearStart(ptr ptr) icu.udat_get2DigitYearStart
133 cdecl udat_getAvailable(long) icu.udat_getAvailable
134 cdecl udat_getBooleanAttribute(ptr long ptr) icu.udat_getBooleanAttribute
135 cdecl udat_getCalendar(ptr) icu.udat_getCalendar
136 cdecl udat_getContext(ptr long ptr) icu.udat_getContext
137 cdecl udat_getLocaleByType(ptr long ptr) icu.udat_getLocaleByType
138 cdecl udat_getNumberFormat(ptr) icu.udat_getNumberFormat
139 cdecl udat_getNumberFormatForField(ptr long) icu.udat_getNumberFormatForField
140 cdecl udat_getSymbols(ptr long long ptr long ptr) icu.udat_getSymbols
141 cdecl udat_isLenient(ptr) icu.udat_isLenient
142 cdecl udat_open(long long str ptr long ptr long ptr) icu.udat_open
143 cdecl udat_parse(ptr ptr long ptr ptr) icu.udat_parse
144 cdecl udat_parseCalendar(ptr ptr ptr long ptr ptr) icu.udat_parseCalendar
145 cdecl udat_set2DigitYearStart(ptr long ptr) icu.udat_set2DigitYearStart
146 cdecl udat_setBooleanAttribute(ptr long long ptr) icu.udat_setBooleanAttribute
147 cdecl udat_setCalendar(ptr ptr) icu.udat_setCalendar
148 cdecl udat_setContext(ptr long ptr) icu.udat_setContext
149 cdecl udat_setLenient(ptr long) icu.udat_setLenient
150 cdecl udat_setNumberFormat(ptr ptr) icu.udat_setNumberFormat
151 cdecl udat_setSymbols(ptr long long ptr long ptr) icu.udat_setSymbols
152 cdecl udat_toCalendarDateField(long) icu.udat_toCalendarDateField
153 cdecl udat_toPattern(ptr long ptr long ptr) icu.udat_toPattern
154 cdecl udatpg_addPattern(ptr ptr long long ptr long ptr ptr) icu.udatpg_addPattern
155 cdecl udatpg_clone(ptr ptr) icu.udatpg_clone
156 cdecl udatpg_close(ptr) icu.udatpg_close
157 cdecl udatpg_getAppendItemFormat(ptr long ptr) icu.udatpg_getAppendItemFormat
158 cdecl udatpg_getAppendItemName(ptr long ptr) icu.udatpg_getAppendItemName
159 cdecl udatpg_getBaseSkeleton(ptr ptr long ptr long ptr) icu.udatpg_getBaseSkeleton
160 cdecl udatpg_getBestPattern(ptr ptr long ptr long ptr) icu.udatpg_getBestPattern
161 cdecl udatpg_getBestPatternWithOptions(ptr ptr long long ptr long ptr) icu.udatpg_getBestPatternWithOptions
162 cdecl udatpg_getDateTimeFormat(ptr ptr) icu.udatpg_getDateTimeFormat
163 cdecl udatpg_getDecimal(ptr ptr) icu.udatpg_getDecimal
164 cdecl udatpg_getPatternForSkeleton(ptr ptr long ptr) icu.udatpg_getPatternForSkeleton
165 cdecl udatpg_getSkeleton(ptr ptr long ptr long ptr) icu.udatpg_getSkeleton
166 cdecl udatpg_open(str ptr) icu.udatpg_open
167 cdecl udatpg_openBaseSkeletons(ptr ptr) icu.udatpg_openBaseSkeletons
168 cdecl udatpg_openEmpty(ptr) icu.udatpg_openEmpty
169 cdecl udatpg_openSkeletons(ptr ptr) icu.udatpg_openSkeletons
170 cdecl udatpg_replaceFieldTypes(ptr ptr long ptr long ptr long ptr) icu.udatpg_replaceFieldTypes
171 cdecl udatpg_replaceFieldTypesWithOptions(ptr ptr long ptr long long ptr long ptr) icu.udatpg_replaceFieldTypesWithOptions
172 cdecl udatpg_setAppendItemFormat(ptr long ptr long) icu.udatpg_setAppendItemFormat
173 cdecl udatpg_setAppendItemName(ptr long ptr long) icu.udatpg_setAppendItemName
174 cdecl udatpg_setDateTimeFormat(ptr ptr long) icu.udatpg_setDateTimeFormat
175 cdecl udatpg_setDecimal(ptr ptr long) icu.udatpg_setDecimal
176 cdecl udtitvfmt_close(ptr) icu.udtitvfmt_close
177 cdecl udtitvfmt_format(ptr long long ptr long ptr ptr) icu.udtitvfmt_format
178 cdecl udtitvfmt_open(str ptr long ptr long ptr) icu.udtitvfmt_open
179 cdecl ufieldpositer_close(ptr) icu.ufieldpositer_close
180 cdecl ufieldpositer_next(ptr ptr ptr) icu.ufieldpositer_next
181 cdecl ufieldpositer_open(ptr) icu.ufieldpositer_open
182 cdecl ufmt_close(ptr) icu.ufmt_close
183 cdecl ufmt_getArrayItemByIndex(ptr long ptr) icu.ufmt_getArrayItemByIndex
184 cdecl ufmt_getArrayLength(ptr ptr) icu.ufmt_getArrayLength
185 cdecl ufmt_getDate(ptr ptr) icu.ufmt_getDate
186 cdecl ufmt_getDecNumChars(ptr ptr ptr) icu.ufmt_getDecNumChars
187 cdecl ufmt_getDouble(ptr ptr) icu.ufmt_getDouble
188 cdecl ufmt_getInt64(ptr ptr) icu.ufmt_getInt64
189 cdecl ufmt_getLong(ptr ptr) icu.ufmt_getLong
190 cdecl ufmt_getObject(ptr ptr) icu.ufmt_getObject
191 cdecl ufmt_getType(ptr ptr) icu.ufmt_getType
192 cdecl ufmt_getUChars(ptr ptr ptr) icu.ufmt_getUChars
193 cdecl ufmt_isNumeric(ptr) icu.ufmt_isNumeric
194 cdecl ufmt_open(ptr) icu.ufmt_open
195 cdecl ugender_getInstance(str ptr) icu.ugender_getInstance
196 cdecl ugender_getListGender(ptr ptr long ptr) icu.ugender_getListGender
197 cdecl ulocdata_close(ptr) icu.ulocdata_close
198 cdecl ulocdata_getCLDRVersion(long ptr) icu.ulocdata_getCLDRVersion
199 cdecl ulocdata_getDelimiter(ptr long ptr long ptr) icu.ulocdata_getDelimiter
200 cdecl ulocdata_getExemplarSet(ptr ptr long long ptr) icu.ulocdata_getExemplarSet
201 cdecl ulocdata_getLocaleDisplayPattern(ptr ptr long ptr) icu.ulocdata_getLocaleDisplayPattern
202 cdecl ulocdata_getLocaleSeparator(ptr ptr long ptr) icu.ulocdata_getLocaleSeparator
203 cdecl ulocdata_getMeasurementSystem(str ptr) icu.ulocdata_getMeasurementSystem
204 cdecl ulocdata_getNoSubstitute(ptr) icu.ulocdata_getNoSubstitute
205 cdecl ulocdata_getPaperSize(str ptr ptr ptr) icu.ulocdata_getPaperSize
206 cdecl ulocdata_open(str ptr) icu.ulocdata_open
207 cdecl ulocdata_setNoSubstitute(ptr long) icu.ulocdata_setNoSubstitute
208 cdecl umsg_applyPattern(ptr ptr long ptr ptr) icu.umsg_applyPattern
209 cdecl umsg_autoQuoteApostrophe(ptr long ptr long ptr) icu.umsg_autoQuoteApostrophe
210 cdecl umsg_clone(ptr ptr) icu.umsg_clone
211 cdecl umsg_close(ptr) icu.umsg_close
212 varargs umsg_format(ptr ptr long ptr) icu.umsg_format
213 cdecl umsg_getLocale(ptr) icu.umsg_getLocale
214 cdecl umsg_open(ptr long str ptr ptr) icu.umsg_open
215 varargs umsg_parse(ptr ptr long ptr ptr) icu.umsg_parse
216 cdecl umsg_setLocale(ptr str) icu.umsg_setLocale
217 cdecl umsg_toPattern(ptr ptr long ptr) icu.umsg_toPattern
218 cdecl umsg_vformat(ptr ptr long long ptr) icu.umsg_vformat
219 cdecl umsg_vparse(ptr ptr long ptr long ptr) icu.umsg_vparse
220 cdecl unum_applyPattern(ptr long ptr long ptr ptr) icu.unum_applyPattern
221 cdecl unum_clone(ptr ptr) icu.unum_clone
222 cdecl unum_close(ptr) icu.unum_close
223 cdecl unum_countAvailable() icu.unum_countAvailable
224 cdecl unum_format(ptr long ptr long ptr ptr) icu.unum_format
225 cdecl unum_formatDecimal(ptr str long ptr long ptr ptr) icu.unum_formatDecimal
226 cdecl unum_formatDouble(ptr double ptr long ptr ptr) icu.unum_formatDouble
227 cdecl unum_formatDoubleCurrency(ptr double ptr ptr long ptr ptr) icu.unum_formatDoubleCurrency
228 cdecl unum_formatDoubleForFields(ptr double ptr long ptr ptr) icu.unum_formatDoubleForFields
229 cdecl unum_formatInt64(ptr long ptr long ptr ptr) icu.unum_formatInt64
230 cdecl unum_formatUFormattable(ptr ptr ptr long ptr ptr) icu.unum_formatUFormattable
231 cdecl unum_getAttribute(ptr long) icu.unum_getAttribute
232 cdecl unum_getAvailable(long) icu.unum_getAvailable
233 cdecl unum_getContext(ptr long ptr) icu.unum_getContext
234 cdecl unum_getDoubleAttribute(ptr long) icu.unum_getDoubleAttribute
235 cdecl unum_getLocaleByType(ptr long ptr) icu.unum_getLocaleByType
236 cdecl unum_getSymbol(ptr long ptr long ptr) icu.unum_getSymbol
237 cdecl unum_getTextAttribute(ptr long ptr long ptr) icu.unum_getTextAttribute
238 cdecl unum_open(long ptr long str ptr ptr) icu.unum_open
239 cdecl unum_parse(ptr ptr long ptr ptr) icu.unum_parse
240 cdecl unum_parseDecimal(ptr ptr long ptr str long ptr) icu.unum_parseDecimal
241 cdecl unum_parseDouble(ptr ptr long ptr ptr) icu.unum_parseDouble
242 cdecl unum_parseDoubleCurrency(ptr ptr long ptr ptr ptr) icu.unum_parseDoubleCurrency
243 cdecl unum_parseInt64(ptr ptr long ptr ptr) icu.unum_parseInt64
244 cdecl unum_parseToUFormattable(ptr ptr ptr long ptr ptr) icu.unum_parseToUFormattable
245 cdecl unum_setAttribute(ptr long long) icu.unum_setAttribute
246 cdecl unum_setContext(ptr long ptr) icu.unum_setContext
247 cdecl unum_setDoubleAttribute(ptr long double) icu.unum_setDoubleAttribute
248 cdecl unum_setSymbol(ptr long ptr long ptr) icu.unum_setSymbol
249 cdecl unum_setTextAttribute(ptr long ptr long ptr) icu.unum_setTextAttribute
250 cdecl unum_toPattern(ptr long ptr long ptr) icu.unum_toPattern
251 cdecl unumsys_close(ptr) icu.unumsys_close
252 cdecl unumsys_getDescription(ptr ptr long ptr) icu.unumsys_getDescription
253 cdecl unumsys_getName(ptr) icu.unumsys_getName
254 cdecl unumsys_getRadix(ptr) icu.unumsys_getRadix
255 cdecl unumsys_isAlgorithmic(ptr) icu.unumsys_isAlgorithmic
256 cdecl unumsys_open(str ptr) icu.unumsys_open
257 cdecl unumsys_openAvailableNames(ptr) icu.unumsys_openAvailableNames
258 cdecl unumsys_openByName(str ptr) icu.unumsys_openByName
259 cdecl uplrules_close(ptr) icu.uplrules_close
260 cdecl uplrules_getKeywords(ptr ptr) icu.uplrules_getKeywords
261 cdecl uplrules_open(str ptr) icu.uplrules_open
262 cdecl uplrules_openForType(str long ptr) icu.uplrules_openForType
263 cdecl uplrules_select(ptr double ptr long ptr) icu.uplrules_select
264 cdecl uregex_appendReplacement(ptr ptr long ptr ptr ptr) icu.uregex_appendReplacement
265 cdecl uregex_appendReplacementUText(ptr ptr ptr ptr) icu.uregex_appendReplacementUText
266 cdecl uregex_appendTail(ptr ptr ptr ptr) icu.uregex_appendTail
267 cdecl uregex_appendTailUText(ptr ptr ptr) icu.uregex_appendTailUText
268 cdecl uregex_clone(ptr ptr) icu.uregex_clone
269 cdecl uregex_close(ptr) icu.uregex_close
270 cdecl uregex_end(ptr long ptr) icu.uregex_end
271 cdecl uregex_end64(ptr long ptr) icu.uregex_end64
272 cdecl uregex_find(ptr long ptr) icu.uregex_find
273 cdecl uregex_find64(ptr long ptr) icu.uregex_find64
274 cdecl uregex_findNext(ptr ptr) icu.uregex_findNext
275 cdecl uregex_flags(ptr ptr) icu.uregex_flags
276 cdecl uregex_getFindProgressCallback(ptr ptr ptr ptr) icu.uregex_getFindProgressCallback
277 cdecl uregex_getMatchCallback(ptr ptr ptr ptr) icu.uregex_getMatchCallback
278 cdecl uregex_getStackLimit(ptr ptr) icu.uregex_getStackLimit
279 cdecl uregex_getText(ptr ptr ptr) icu.uregex_getText
280 cdecl uregex_getTimeLimit(ptr ptr) icu.uregex_getTimeLimit
281 cdecl uregex_getUText(ptr ptr ptr) icu.uregex_getUText
282 cdecl uregex_group(ptr long ptr long ptr) icu.uregex_group
283 cdecl uregex_groupCount(ptr ptr) icu.uregex_groupCount
284 cdecl uregex_groupNumberFromCName(ptr str long ptr) icu.uregex_groupNumberFromCName
285 cdecl uregex_groupNumberFromName(ptr ptr long ptr) icu.uregex_groupNumberFromName
286 cdecl uregex_groupUText(ptr long ptr ptr ptr) icu.uregex_groupUText
287 cdecl uregex_hasAnchoringBounds(ptr ptr) icu.uregex_hasAnchoringBounds
288 cdecl uregex_hasTransparentBounds(ptr ptr) icu.uregex_hasTransparentBounds
289 cdecl uregex_hitEnd(ptr ptr) icu.uregex_hitEnd
290 cdecl uregex_lookingAt(ptr long ptr) icu.uregex_lookingAt
291 cdecl uregex_lookingAt64(ptr long ptr) icu.uregex_lookingAt64
292 cdecl uregex_matches(ptr long ptr) icu.uregex_matches
293 cdecl uregex_matches64(ptr long ptr) icu.uregex_matches64
294 cdecl uregex_open(ptr long long ptr ptr) icu.uregex_open
295 cdecl uregex_openC(str long ptr ptr) icu.uregex_openC
296 cdecl uregex_openUText(ptr long ptr ptr) icu.uregex_openUText
297 cdecl uregex_pattern(ptr ptr ptr) icu.uregex_pattern
298 cdecl uregex_patternUText(ptr ptr) icu.uregex_patternUText
299 cdecl uregex_refreshUText(ptr ptr ptr) icu.uregex_refreshUText
300 cdecl uregex_regionEnd(ptr ptr) icu.uregex_regionEnd
301 cdecl uregex_regionEnd64(ptr ptr) icu.uregex_regionEnd64
302 cdecl uregex_regionStart(ptr ptr) icu.uregex_regionStart
303 cdecl uregex_regionStart64(ptr ptr) icu.uregex_regionStart64
304 cdecl uregex_replaceAll(ptr ptr long ptr long ptr) icu.uregex_replaceAll
305 cdecl uregex_replaceAllUText(ptr ptr ptr ptr) icu.uregex_replaceAllUText
306 cdecl uregex_replaceFirst(ptr ptr long ptr long ptr) icu.uregex_replaceFirst
307 cdecl uregex_replaceFirstUText(ptr ptr ptr ptr) icu.uregex_replaceFirstUText
308 cdecl uregex_requireEnd(ptr ptr) icu.uregex_requireEnd
309 cdecl uregex_reset(ptr long ptr) icu.uregex_reset
310 cdecl uregex_reset64(ptr long ptr) icu.uregex_reset64
311 cdecl uregex_setFindProgressCallback(ptr ptr ptr ptr) icu.uregex_setFindProgressCallback
312 cdecl uregex_setMatchCallback(ptr ptr ptr ptr) icu.uregex_setMatchCallback
313 cdecl uregex_setRegion(ptr long long ptr) icu.uregex_setRegion
314 cdecl uregex_setRegion64(ptr long long ptr) icu.uregex_setRegion64
315 cdecl uregex_setRegionAndStart(ptr long long long ptr) icu.uregex_setRegionAndStart
316 cdecl uregex_setStackLimit(ptr long ptr) icu.uregex_setStackLimit
317 cdecl uregex_setText(ptr ptr long ptr) icu.uregex_setText
318 cdecl uregex_setTimeLimit(ptr long ptr) icu.uregex_setTimeLimit
319 cdecl uregex_setUText(ptr ptr ptr) icu.uregex_setUText
320 cdecl uregex_split(ptr ptr long ptr ptr long ptr) icu.uregex_split
321 cdecl uregex_splitUText(ptr ptr long ptr) icu.uregex_splitUText
322 cdecl uregex_start(ptr long ptr) icu.uregex_start
323 cdecl uregex_start64(ptr long ptr) icu.uregex_start64
324 cdecl uregex_useAnchoringBounds(ptr long ptr) icu.uregex_useAnchoringBounds
325 cdecl uregex_useTransparentBounds(ptr long ptr) icu.uregex_useTransparentBounds
326 cdecl uregion_areEqual(ptr ptr) icu.uregion_areEqual
327 cdecl uregion_contains(ptr ptr) icu.uregion_contains
328 cdecl uregion_getAvailable(long ptr) icu.uregion_getAvailable
329 cdecl uregion_getContainedRegions(ptr ptr) icu.uregion_getContainedRegions
330 cdecl uregion_getContainedRegionsOfType(ptr long ptr) icu.uregion_getContainedRegionsOfType
331 cdecl uregion_getContainingRegion(ptr) icu.uregion_getContainingRegion
332 cdecl uregion_getContainingRegionOfType(ptr long) icu.uregion_getContainingRegionOfType
333 cdecl uregion_getNumericCode(ptr) icu.uregion_getNumericCode
334 cdecl uregion_getPreferredValues(ptr ptr) icu.uregion_getPreferredValues
335 cdecl uregion_getRegionCode(ptr) icu.uregion_getRegionCode
336 cdecl uregion_getRegionFromCode(str ptr) icu.uregion_getRegionFromCode
337 cdecl uregion_getRegionFromNumericCode(long ptr) icu.uregion_getRegionFromNumericCode
338 cdecl uregion_getType(ptr) icu.uregion_getType
339 cdecl ureldatefmt_close(ptr) icu.ureldatefmt_close
340 cdecl ureldatefmt_combineDateAndTime(ptr ptr long ptr long ptr long ptr) icu.ureldatefmt_combineDateAndTime
341 cdecl ureldatefmt_format(ptr double long ptr long ptr) icu.ureldatefmt_format
342 cdecl ureldatefmt_formatNumeric(ptr double long ptr long ptr) icu.ureldatefmt_formatNumeric
343 cdecl ureldatefmt_open(str ptr long long ptr) icu.ureldatefmt_open
344 cdecl usearch_close(ptr) icu.usearch_close
345 cdecl usearch_first(ptr ptr) icu.usearch_first
346 cdecl usearch_following(ptr long ptr) icu.usearch_following
347 cdecl usearch_getAttribute(ptr long) icu.usearch_getAttribute
348 cdecl usearch_getBreakIterator(ptr) icu.usearch_getBreakIterator
349 cdecl usearch_getCollator(ptr) icu.usearch_getCollator
350 cdecl usearch_getMatchedLength(ptr) icu.usearch_getMatchedLength
351 cdecl usearch_getMatchedStart(ptr) icu.usearch_getMatchedStart
352 cdecl usearch_getMatchedText(ptr ptr long ptr) icu.usearch_getMatchedText
353 cdecl usearch_getOffset(ptr) icu.usearch_getOffset
354 cdecl usearch_getPattern(ptr ptr) icu.usearch_getPattern
355 cdecl usearch_getText(ptr ptr) icu.usearch_getText
356 cdecl usearch_last(ptr ptr) icu.usearch_last
357 cdecl usearch_next(ptr ptr) icu.usearch_next
358 cdecl usearch_open(ptr long ptr long str ptr ptr) icu.usearch_open
359 cdecl usearch_openFromCollator(ptr long ptr long ptr ptr ptr) icu.usearch_openFromCollator
360 cdecl usearch_preceding(ptr long ptr) icu.usearch_preceding
361 cdecl usearch_previous(ptr ptr) icu.usearch_previous
362 cdecl usearch_reset(ptr) icu.usearch_reset
363 cdecl usearch_setAttribute(ptr long long ptr) icu.usearch_setAttribute
364 cdecl usearch_setBreakIterator(ptr ptr ptr) icu.usearch_setBreakIterator
365 cdecl usearch_setCollator(ptr ptr ptr) icu.usearch_setCollator
366 cdecl usearch_setOffset(ptr long ptr) icu.usearch_setOffset
367 cdecl usearch_setPattern(ptr ptr long ptr) icu.usearch_setPattern
368 cdecl usearch_setText(ptr ptr long ptr) icu.usearch_setText
369 cdecl uspoof_areConfusable(ptr ptr long ptr long ptr) icu.uspoof_areConfusable
370 cdecl uspoof_areConfusableUTF8(ptr str long str long ptr) icu.uspoof_areConfusableUTF8
371 cdecl uspoof_check(ptr ptr long ptr ptr) icu.uspoof_check
372 cdecl uspoof_check2(ptr ptr long ptr ptr) icu.uspoof_check2
373 cdecl uspoof_check2UTF8(ptr str long ptr ptr) icu.uspoof_check2UTF8
374 cdecl uspoof_checkUTF8(ptr str long ptr ptr) icu.uspoof_checkUTF8
375 cdecl uspoof_clone(ptr ptr) icu.uspoof_clone
376 cdecl uspoof_close(ptr) icu.uspoof_close
377 cdecl uspoof_closeCheckResult(ptr) icu.uspoof_closeCheckResult
378 cdecl uspoof_getAllowedChars(ptr ptr) icu.uspoof_getAllowedChars
379 cdecl uspoof_getAllowedLocales(ptr ptr) icu.uspoof_getAllowedLocales
380 cdecl uspoof_getCheckResultChecks(ptr ptr) icu.uspoof_getCheckResultChecks
381 cdecl uspoof_getCheckResultNumerics(ptr ptr) icu.uspoof_getCheckResultNumerics
382 cdecl uspoof_getCheckResultRestrictionLevel(ptr ptr) icu.uspoof_getCheckResultRestrictionLevel
383 cdecl uspoof_getChecks(ptr ptr) icu.uspoof_getChecks
384 cdecl uspoof_getInclusionSet(ptr) icu.uspoof_getInclusionSet
385 cdecl uspoof_getRecommendedSet(ptr) icu.uspoof_getRecommendedSet
386 cdecl uspoof_getRestrictionLevel(ptr) icu.uspoof_getRestrictionLevel
387 cdecl uspoof_getSkeleton(ptr long ptr long ptr long ptr) icu.uspoof_getSkeleton
388 cdecl uspoof_getSkeletonUTF8(ptr long str long str long ptr) icu.uspoof_getSkeletonUTF8
389 cdecl uspoof_open(ptr) icu.uspoof_open
390 cdecl uspoof_openCheckResult(ptr) icu.uspoof_openCheckResult
391 cdecl uspoof_openFromSerialized(ptr long ptr ptr) icu.uspoof_openFromSerialized
392 cdecl uspoof_openFromSource(str long str long ptr ptr ptr) icu.uspoof_openFromSource
393 cdecl uspoof_serialize(ptr ptr long ptr) icu.uspoof_serialize
394 cdecl uspoof_setAllowedChars(ptr ptr ptr) icu.uspoof_setAllowedChars
395 cdecl uspoof_setAllowedLocales(ptr str ptr) icu.uspoof_setAllowedLocales
396 cdecl uspoof_setChecks(ptr long ptr) icu.uspoof_setChecks
397 cdecl uspoof_setRestrictionLevel(ptr long) icu.uspoof_setRestrictionLevel
398 cdecl utmscale_fromInt64(long long ptr) icu.utmscale_fromInt64
399 cdecl utmscale_getTimeScaleValue(long long ptr) icu.utmscale_getTimeScaleValue
400 cdecl utmscale_toInt64(long long ptr) icu.utmscale_toInt64
401 cdecl utrans_clone(ptr ptr) icu.utrans_clone
402 cdecl utrans_close(ptr) icu.utrans_close
403 cdecl utrans_countAvailableIDs() icu.utrans_countAvailableIDs
404 cdecl utrans_getSourceSet(ptr long ptr ptr) icu.utrans_getSourceSet
405 cdecl utrans_getUnicodeID(ptr ptr) icu.utrans_getUnicodeID
406 cdecl utrans_openIDs(ptr) icu.utrans_openIDs
407 cdecl utrans_openInverse(ptr ptr) icu.utrans_openInverse
408 cdecl utrans_openU(ptr long long ptr long ptr ptr) icu.utrans_openU
409 cdecl utrans_register(ptr ptr) icu.utrans_register
410 cdecl utrans_setFilter(ptr ptr long ptr) icu.utrans_setFilter
411 cdecl utrans_toRules(ptr long ptr long ptr) icu.utrans_toRules
412 cdecl utrans_trans(ptr ptr ptr long ptr ptr) icu.utrans_trans
413 cdecl utrans_transIncremental(ptr ptr ptr ptr ptr) icu.utrans_transIncremental
414 cdecl utrans_transIncrementalUChars(ptr ptr ptr long ptr ptr) icu.utrans_transIncrementalUChars
415 cdecl utrans_transUChars(ptr ptr ptr long long ptr ptr) icu.utrans_transUChars
416 cdecl utrans_unregisterID(ptr long) icu.utrans_unregisterID
