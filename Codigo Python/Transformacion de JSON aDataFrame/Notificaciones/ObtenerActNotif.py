import pandas as pd
def getNotif(df2):
    r1 = df2.loc[:, 'dspId'] == 1060
    r2 = df2.loc[:, 'dspId'] == 1143
    r3 = df2.loc[:, 'dspId'] == 1062
    r4 = df2.loc[:, 'dspId'] == 1061
    r5 = df2.loc[:, 'dspId'] == 1107
    r6 = df2.loc[:, 'dspId'] == 1197
    r7 = df2.loc[:, 'dspId'] == 1477
    r8 = df2.loc[:, 'dspId'] == 1188
    r9 = df2.loc[:, 'dspId'] == 1073
    r10 = df2.loc[:, 'dspId'] == 1262
    r11 = df2.loc[:, 'dspId'] == 1344
    r12 = df2.loc[:, 'dspId'] == 1140
    r13 = df2.loc[:, 'dspId'] == 1066
    r14 = df2.loc[:, 'dspId'] == 1070
    r15 = df2.loc[:, 'dspId'] == 1273
    r16 = df2.loc[:, 'dspId'] == 1535
    r17 = df2.loc[:, 'dspId'] == 1225
    r18 = df2.loc[:, 'dspId'] == 1118
    r19 = df2.loc[:, 'dspId'] == 1071
    r20 = df2.loc[:, 'dspId'] == 1080
    r21 = df2.loc[:, 'dspId'] == 1193
    r22 = df2.loc[:, 'dspId'] == 1064
    r23 = df2.loc[:, 'dspId'] == 1425
    r24 = df2.loc[:, 'dspId'] == 1065
    r25 = df2.loc[:, 'dspId'] == 1301
    r26 = df2.loc[:, 'dspId'] == 1621
    r27 = df2.loc[:, 'dspId'] == 1059
    r28 = df2.loc[:, 'dspId'] == 1555
    r29 = df2.loc[:, 'dspId'] == 1618
    r30 = df2.loc[:, 'dspId'] == 1472
    r31 = df2.loc[:, 'dspId'] == 1631
    r32 = df2.loc[:, 'dspId'] == 1147
    r33 = df2.loc[:, 'dspId'] == 1520
    r34 = df2.loc[:, 'dspId'] == 1328
    r35 = df2.loc[:, 'dspId'] == 1275
    r36 = df2.loc[:, 'dspId'] == 1068
    r37 = df2.loc[:, 'dspId'] == 1316
    r38 = df2.loc[:, 'dspId'] == 1338
    r39 = df2.loc[:, 'dspId'] == 1720
    r40 = df2.loc[:, 'dspId'] == 1412
    r41 = df2.loc[:, 'dspId'] == 1286
    r42 = df2.loc[:, 'dspId'] == 1723
    r43 = df2.loc[:, 'dspId'] == 1459
    r44 = df2.loc[:, 'dspId'] == 1134
    r45 = df2.loc[:, 'dspId'] == 1287
    r46 = df2.loc[:, 'dspId'] == 1148
    r47 = df2.loc[:, 'dspId'] == 1128
    r48 = df2.loc[:, 'dspId'] == 1439
    r49 = df2.loc[:, 'dspId'] == 1096
    r50 = df2.loc[:, 'dspId'] == 1237
    r51 = df2.loc[:, 'dspId'] == 1311
    r52 = df2.loc[:, 'dspId'] == 1552
    r53 = df2.loc[:, 'dspId'] == 1186
    r54 = df2.loc[:, 'dspId'] == 1069
    r55 = df2.loc[:, 'dspId'] == 1101
    r56 = df2.loc[:, 'dspId'] == 1102
    r57 = df2.loc[:, 'dspId'] == 1696
    r58 = df2.loc[:, 'dspId'] == 1184
    r59 = df2.loc[:, 'dspId'] == 1321
    r60 = df2.loc[:, 'dspId'] == 1329
    r61 = df2.loc[:, 'dspId'] == 1174
    r62 = df2.loc[:, 'dspId'] == 1343
    r63 = df2.loc[:, 'dspId'] == 1701
    r64 = df2.loc[:, 'dspId'] == 1131
    r65 = df2.loc[:, 'dspId'] == 1684
    r66 = df2.loc[:, 'dspId'] == 1153
    r67 = df2.loc[:, 'dspId'] == 1178
    r68 = df2.loc[:, 'dspId'] == 1189
    r69 = df2.loc[:, 'dspId'] == 1215
    r70 = df2.loc[:, 'dspId'] == 1132
    r71 = df2.loc[:, 'dspId'] == 1051
    r72 = df2.loc[:, 'dspId'] == 1515
    r73 = df2.loc[:, 'dspId'] == 1452
    r74 = df2.loc[:, 'dspId'] == 1417
    r75 = df2.loc[:, 'dspId'] == 1634
    r76 = df2.loc[:, 'dspId'] == 1526
    r77 = df2.loc[:, 'dspId'] == 1330
    r78 = df2.loc[:, 'dspId'] == 1332
    r79 = df2.loc[:, 'dspId'] == 1365
    r80 = df2.loc[:, 'dspId'] == 1556
    r81 = df2.loc[:, 'dspId'] == 1307
    r82 = df2.loc[:, 'dspId'] == 1430
    r83 = df2.loc[:, 'dspId'] == 1187
    r84 = df2.loc[:, 'dspId'] == 1304
    r85 = df2.loc[:, 'dspId'] == 1660
    r86 = df2.loc[:, 'dspId'] == 1158
    r87 = df2.loc[:, 'dspId'] == 1167
    r88 = df2.loc[:, 'dspId'] == 1322
    r89 = df2.loc[:, 'dspId'] == 1192
    r90 = df2.loc[:, 'dspId'] == 1508
    r91 = df2.loc[:, 'dspId'] == 1317
    r92 = df2.loc[:, 'dspId'] == 1534
    r93 = df2.loc[:, 'dspId'] == 1457
    r94 = df2.loc[:, 'dspId'] == 1110
    r95 = df2.loc[:, 'dspId'] == 1605
    r96 = df2.loc[:, 'dspId'] == 1371
    r97 = df2.loc[:, 'dspId'] == 1055
    r98 = df2.loc[:, 'dspId'] == 1161
    r99 = df2.loc[:, 'dspId'] == 1691
    r100 = df2.loc[:, 'dspId'] == 1367
    r101 = df2.loc[:, 'dspId'] == 1336
    r102 = df2.loc[:, 'dspId'] == 1302
    r103 = df2.loc[:, 'dspId'] == 1104
    r104 = df2.loc[:, 'dspId'] == 1337
    r105 = df2.loc[:, 'dspId'] == 1133
    r106 = df2.loc[:, 'dspId'] == 1185
    r107 = df2.loc[:, 'dspId'] == 1428
    r108 = df2.loc[:, 'dspId'] == 1715
    r109 = df2.loc[:, 'dspId'] == 1401
    r110 = df2.loc[:, 'dspId'] == 1378
    r111 = df2.loc[:, 'dspId'] == 1640
    r112 = df2.loc[:, 'dspId'] == 1370
    r113 = df2.loc[:, 'dspId'] == 1135
    r114 = df2.loc[:, 'dspId'] == 1144
    r115 = df2.loc[:, 'dspId'] == 1308
    r116 = df2.loc[:, 'dspId'] == 1249
    r117 = df2.loc[:, 'dspId'] == 1366
    r118 = df2.loc[:, 'dspId'] == 1601
    r119 = df2.loc[:, 'dspId'] == 1474
    r120 = df2.loc[:, 'dspId'] == 1538
    r121 = df2.loc[:, 'dspId'] == 1714
    r122 = df2.loc[:, 'dspId'] == 1272
    r123 = df2.loc[:, 'dspId'] == 1163
    r124 = df2.loc[:, 'dspId'] == 1637
    r125 = df2.loc[:, 'dspId'] == 1285
    r126 = df2.loc[:, 'dspId'] == 1278
    r127 = df2.loc[:, 'dspId'] == 1112
    r128 = df2.loc[:, 'dspId'] == 1705
    r129 = df2.loc[:, 'dspId'] == 1280
    r130 = df2.loc[:, 'dspId'] == 1725

    s1 = df2.loc[r1]
    s2 = df2.loc[r2]
    s3 = df2.loc[r3]
    s4 = df2.loc[r4]
    s5 = df2.loc[r5]
    s6 = df2.loc[r6]
    s7 = df2.loc[r7]
    s8 = df2.loc[r8]
    s9 = df2.loc[r9]
    s10 = df2.loc[r10]
    s11 = df2.loc[r11]
    s12 = df2.loc[r12]
    s13 = df2.loc[r13]
    s14 = df2.loc[r14]
    s15 = df2.loc[r15]
    s16 = df2.loc[r16]
    s17 = df2.loc[r17]
    s18 = df2.loc[r18]
    s19 = df2.loc[r19]
    s20 = df2.loc[r20]
    s21 = df2.loc[r21]
    s22 = df2.loc[r22]
    s23 = df2.loc[r23]
    s24 = df2.loc[r24]
    s25 = df2.loc[r25]
    s26 = df2.loc[r26]
    s27 = df2.loc[r27]
    s28 = df2.loc[r28]
    s29 = df2.loc[r29]
    s30 = df2.loc[r30]
    s31 = df2.loc[r31]
    s32 = df2.loc[r32]
    s33 = df2.loc[r33]
    s34 = df2.loc[r34]
    s35 = df2.loc[r35]
    s36 = df2.loc[r36]
    s37 = df2.loc[r37]
    s38 = df2.loc[r38]
    s39 = df2.loc[r39]
    s40 = df2.loc[r40]
    s41 = df2.loc[r41]
    s42 = df2.loc[r42]
    s43 = df2.loc[r43]
    s44 = df2.loc[r44]
    s45 = df2.loc[r45]
    s46 = df2.loc[r46]
    s47 = df2.loc[r47]
    s48 = df2.loc[r48]
    s49 = df2.loc[r49]
    s50 = df2.loc[r50]
    s51 = df2.loc[r51]
    s52 = df2.loc[r52]
    s53 = df2.loc[r53]
    s54 = df2.loc[r54]
    s55 = df2.loc[r55]
    s56 = df2.loc[r56]
    s57 = df2.loc[r57]
    s58 = df2.loc[r58]
    s59 = df2.loc[r59]
    s60 = df2.loc[r60]
    s61 = df2.loc[r61]
    s62 = df2.loc[r62]
    s63 = df2.loc[r63]
    s64 = df2.loc[r64]
    s65 = df2.loc[r65]
    s66 = df2.loc[r66]
    s67 = df2.loc[r67]
    s68 = df2.loc[r68]
    s69 = df2.loc[r69]
    s70 = df2.loc[r70]
    s71 = df2.loc[r71]
    s72 = df2.loc[r72]
    s73 = df2.loc[r73]
    s74 = df2.loc[r74]
    s75 = df2.loc[r75]
    s76 = df2.loc[r76]
    s77 = df2.loc[r77]
    s78 = df2.loc[r78]
    s79 = df2.loc[r79]
    s80 = df2.loc[r80]
    s81 = df2.loc[r81]
    s82 = df2.loc[r82]
    s83 = df2.loc[r83]
    s84 = df2.loc[r84]
    s85 = df2.loc[r85]
    s86 = df2.loc[r86]
    s87 = df2.loc[r87]
    s88 = df2.loc[r88]
    s89 = df2.loc[r89]
    s90 = df2.loc[r90]
    s91 = df2.loc[r91]
    s92 = df2.loc[r92]
    s93 = df2.loc[r93]
    s94 = df2.loc[r94]
    s95 = df2.loc[r95]
    s96 = df2.loc[r96]
    s97 = df2.loc[r97]
    s98 = df2.loc[r98]
    s99 = df2.loc[r99]
    s100 = df2.loc[r100]
    s101 = df2.loc[r101]
    s102 = df2.loc[r102]
    s103 = df2.loc[r103]
    s104 = df2.loc[r104]
    s105 = df2.loc[r105]
    s106 = df2.loc[r106]
    s107 = df2.loc[r107]
    s108 = df2.loc[r108]
    s109 = df2.loc[r109]
    s110 = df2.loc[r110]
    s111 = df2.loc[r111]
    s112 = df2.loc[r112]
    s113 = df2.loc[r113]
    s114 = df2.loc[r114]
    s115 = df2.loc[r115]
    s116 = df2.loc[r116]
    s117 = df2.loc[r117]
    s118 = df2.loc[r118]
    s119 = df2.loc[r119]
    s120 = df2.loc[r120]
    s121 = df2.loc[r121]
    s122 = df2.loc[r122]
    s123 = df2.loc[r123]
    s124 = df2.loc[r124]
    s125 = df2.loc[r125]
    s126 = df2.loc[r126]
    s127 = df2.loc[r127]
    s128 = df2.loc[r128]
    s129 = df2.loc[r129]
    s130 = df2.loc[r130]

    final = pd.concat([s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21, s22, s23, s24, s25, s26, s27, s28, s29, s30, s31, s32, s33, s34, s35, s36, s37, s38, s39, s40, s41, s42, s43, s44, s45, s46, s47, s48, s49, s50, s51, s52, s53, s54, s55, s56, s57, s58, s59, s60, s61, s62, s63, s64, s65, s66, s67, s68, s69, s70, s71, s72, s73, s74, s75, s76, s77, s78, s79, s80, s81, s82, s83, s84, s85, s86, s87, s88, s89, s90, s91, s92, s93, s94, s95, s96, s97, s98, s99, s100, s101, s102, s103, s104, s105, s106, s107, s108, s109, s110, s111, s112, s113, s114, s115, s116, s117, s118, s119, s120, s121, s122, s123, s124, s125, s126, s127, s128, s129, s130])
    return final