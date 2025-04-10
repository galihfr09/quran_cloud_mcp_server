from typing import Literal

quran_details = """Surah Arabic name: سُورَةُ ٱلْفَاتِحَةِ
Surah English name: Al-Faatiha
Surah number: 1
Number of verses: 7
--------------------
Surah Arabic name: سُورَةُ البَقَرَةِ
Surah English name: Al-Baqara
Surah number: 2
Number of verses: 286
--------------------
Surah Arabic name: سُورَةُ آلِ عِمۡرَانَ
Surah English name: Aal-i-Imraan
Surah number: 3
Number of verses: 200
--------------------
Surah Arabic name: سُورَةُ النِّسَاءِ
Surah English name: An-Nisaa
Surah number: 4
Number of verses: 176
--------------------
Surah Arabic name: سُورَةُ المَائـِدَةِ
Surah English name: Al-Maaida
Surah number: 5
Number of verses: 120
--------------------
Surah Arabic name: سُورَةُ الأَنۡعَامِ
Surah English name: Al-An'aam
Surah number: 6
Number of verses: 165
--------------------
Surah Arabic name: سُورَةُ الأَعۡرَافِ
Surah English name: Al-A'raaf
Surah number: 7
Number of verses: 206
--------------------
Surah Arabic name: سُورَةُ الأَنفَالِ
Surah English name: Al-Anfaal
Surah number: 8
Number of verses: 75
--------------------
Surah Arabic name: سُورَةُ التَّوۡبَةِ
Surah English name: At-Tawba
Surah number: 9
Number of verses: 129
--------------------
Surah Arabic name: سُورَةُ يُونُسَ
Surah English name: Yunus
Surah number: 10
Number of verses: 109
--------------------
Surah Arabic name: سُورَةُ هُودٍ
Surah English name: Hud
Surah number: 11
Number of verses: 123
--------------------
Surah Arabic name: سُورَةُ يُوسُفَ
Surah English name: Yusuf
Surah number: 12
Number of verses: 111
--------------------
Surah Arabic name: سُورَةُ الرَّعۡدِ
Surah English name: Ar-Ra'd
Surah number: 13
Number of verses: 43
--------------------
Surah Arabic name: سُورَةُ إِبۡرَاهِيمَ
Surah English name: Ibrahim
Surah number: 14
Number of verses: 52
--------------------
Surah Arabic name: سُورَةُ الحِجۡرِ
Surah English name: Al-Hijr
Surah number: 15
Number of verses: 99
--------------------
Surah Arabic name: سُورَةُ النَّحۡلِ
Surah English name: An-Nahl
Surah number: 16
Number of verses: 128
--------------------
Surah Arabic name: سُورَةُ الإِسۡرَاءِ
Surah English name: Al-Israa
Surah number: 17
Number of verses: 111
--------------------
Surah Arabic name: سُورَةُ الكَهۡفِ
Surah English name: Al-Kahf
Surah number: 18
Number of verses: 110
--------------------
Surah Arabic name: سُورَةُ مَرۡيَمَ
Surah English name: Maryam
Surah number: 19
Number of verses: 98
--------------------
Surah Arabic name: سُورَةُ طه
Surah English name: Taa-Haa
Surah number: 20
Number of verses: 135
--------------------
Surah Arabic name: سُورَةُ الأَنبِيَاءِ
Surah English name: Al-Anbiyaa
Surah number: 21
Number of verses: 112
--------------------
Surah Arabic name: سُورَةُ الحَجِّ
Surah English name: Al-Hajj
Surah number: 22
Number of verses: 78
--------------------
Surah Arabic name: سُورَةُ المُؤۡمِنُونَ
Surah English name: Al-Muminoon
Surah number: 23
Number of verses: 118
--------------------
Surah Arabic name: سُورَةُ النُّورِ
Surah English name: An-Noor
Surah number: 24
Number of verses: 64
--------------------
Surah Arabic name: سُورَةُ الفُرۡقَانِ
Surah English name: Al-Furqaan
Surah number: 25
Number of verses: 77
--------------------
Surah Arabic name: سُورَةُ الشُّعَرَاءِ
Surah English name: Ash-Shu'araa
Surah number: 26
Number of verses: 227
--------------------
Surah Arabic name: سُورَةُ النَّمۡلِ
Surah English name: An-Naml
Surah number: 27
Number of verses: 93
--------------------
Surah Arabic name: سُورَةُ القَصَصِ
Surah English name: Al-Qasas
Surah number: 28
Number of verses: 88
--------------------
Surah Arabic name: سُورَةُ العَنكَبُوتِ
Surah English name: Al-Ankaboot
Surah number: 29
Number of verses: 69
--------------------
Surah Arabic name: سُورَةُ الرُّومِ
Surah English name: Ar-Room
Surah number: 30
Number of verses: 60
--------------------
Surah Arabic name: سُورَةُ لُقۡمَانَ
Surah English name: Luqman
Surah number: 31
Number of verses: 34
--------------------
Surah Arabic name: سُورَةُ السَّجۡدَةِ
Surah English name: As-Sajda
Surah number: 32
Number of verses: 30
--------------------
Surah Arabic name: سُورَةُ الأَحۡزَابِ
Surah English name: Al-Ahzaab
Surah number: 33
Number of verses: 73
--------------------
Surah Arabic name: سُورَةُ سَبَإٍ
Surah English name: Saba
Surah number: 34
Number of verses: 54
--------------------
Surah Arabic name: سُورَةُ فَاطِرٍ
Surah English name: Faatir
Surah number: 35
Number of verses: 45
--------------------
Surah Arabic name: سُورَةُ يسٓ
Surah English name: Yaseen
Surah number: 36
Number of verses: 83
--------------------
Surah Arabic name: سُورَةُ الصَّافَّاتِ
Surah English name: As-Saaffaat
Surah number: 37
Number of verses: 182
--------------------
Surah Arabic name: سُورَةُ صٓ
Surah English name: Saad
Surah number: 38
Number of verses: 88
--------------------
Surah Arabic name: سُورَةُ الزُّمَرِ
Surah English name: Az-Zumar
Surah number: 39
Number of verses: 75
--------------------
Surah Arabic name: سُورَةُ غَافِرٍ
Surah English name: Ghafir
Surah number: 40
Number of verses: 85
--------------------
Surah Arabic name: سُورَةُ فُصِّلَتۡ
Surah English name: Fussilat
Surah number: 41
Number of verses: 54
--------------------
Surah Arabic name: سُورَةُ الشُّورَىٰ
Surah English name: Ash-Shura
Surah number: 42
Number of verses: 53
--------------------
Surah Arabic name: سُورَةُ الزُّخۡرُفِ
Surah English name: Az-Zukhruf
Surah number: 43
Number of verses: 89
--------------------
Surah Arabic name: سُورَةُ الدُّخَانِ
Surah English name: Ad-Dukhaan
Surah number: 44
Number of verses: 59
--------------------
Surah Arabic name: سُورَةُ الجَاثِيَةِ
Surah English name: Al-Jaathiya
Surah number: 45
Number of verses: 37
--------------------
Surah Arabic name: سُورَةُ الأَحۡقَافِ
Surah English name: Al-Ahqaf
Surah number: 46
Number of verses: 35
--------------------
Surah Arabic name: سُورَةُ مُحَمَّدٍ
Surah English name: Muhammad
Surah number: 47
Number of verses: 38
--------------------
Surah Arabic name: سُورَةُ الفَتۡحِ
Surah English name: Al-Fath
Surah number: 48
Number of verses: 29
--------------------
Surah Arabic name: سُورَةُ الحُجُرَاتِ
Surah English name: Al-Hujuraat
Surah number: 49
Number of verses: 18
--------------------
Surah Arabic name: سُورَةُ قٓ
Surah English name: Qaaf
Surah number: 50
Number of verses: 45
--------------------
Surah Arabic name: سُورَةُ الذَّارِيَاتِ
Surah English name: Adh-Dhaariyat
Surah number: 51
Number of verses: 60
--------------------
Surah Arabic name: سُورَةُ الطُّورِ
Surah English name: At-Tur
Surah number: 52
Number of verses: 49
--------------------
Surah Arabic name: سُورَةُ النَّجۡمِ
Surah English name: An-Najm
Surah number: 53
Number of verses: 62
--------------------
Surah Arabic name: سُورَةُ القَمَرِ
Surah English name: Al-Qamar
Surah number: 54
Number of verses: 55
--------------------
Surah Arabic name: سُورَةُ الرَّحۡمَٰن
Surah English name: Ar-Rahmaan
Surah number: 55
Number of verses: 78
--------------------
Surah Arabic name: سُورَةُ الوَاقِعَةِ
Surah English name: Al-Waaqia
Surah number: 56
Number of verses: 96
--------------------
Surah Arabic name: سُورَةُ الحَدِيدِ
Surah English name: Al-Hadid
Surah number: 57
Number of verses: 29
--------------------
Surah Arabic name: سُورَةُ المُجَادلَةِ
Surah English name: Al-Mujaadila
Surah number: 58
Number of verses: 22
--------------------
Surah Arabic name: سُورَةُ الحَشۡرِ
Surah English name: Al-Hashr
Surah number: 59
Number of verses: 24
--------------------
Surah Arabic name: سُورَةُ المُمۡتَحنَةِ
Surah English name: Al-Mumtahana
Surah number: 60
Number of verses: 13
--------------------
Surah Arabic name: سُورَةُ الصَّفِّ
Surah English name: As-Saff
Surah number: 61
Number of verses: 14
--------------------
Surah Arabic name: سُورَةُ الجُمُعَةِ
Surah English name: Al-Jumu'a
Surah number: 62
Number of verses: 11
--------------------
Surah Arabic name: سُورَةُ المُنَافِقُونَ
Surah English name: Al-Munaafiqoon
Surah number: 63
Number of verses: 11
--------------------
Surah Arabic name: سُورَةُ التَّغَابُنِ
Surah English name: At-Taghaabun
Surah number: 64
Number of verses: 18
--------------------
Surah Arabic name: سُورَةُ الطَّلَاقِ
Surah English name: At-Talaaq
Surah number: 65
Number of verses: 12
--------------------
Surah Arabic name: سُورَةُ التَّحۡرِيمِ
Surah English name: At-Tahrim
Surah number: 66
Number of verses: 12
--------------------
Surah Arabic name: سُورَةُ المُلۡكِ
Surah English name: Al-Mulk
Surah number: 67
Number of verses: 30
--------------------
Surah Arabic name: سُورَةُ القَلَمِ
Surah English name: Al-Qalam
Surah number: 68
Number of verses: 52
--------------------
Surah Arabic name: سُورَةُ الحَاقَّةِ
Surah English name: Al-Haaqqa
Surah number: 69
Number of verses: 52
--------------------
Surah Arabic name: سُورَةُ المَعَارِجِ
Surah English name: Al-Ma'aarij
Surah number: 70
Number of verses: 44
--------------------
Surah Arabic name: سُورَةُ نُوحٍ
Surah English name: Nooh
Surah number: 71
Number of verses: 28
--------------------
Surah Arabic name: سُورَةُ الجِنِّ
Surah English name: Al-Jinn
Surah number: 72
Number of verses: 28
--------------------
Surah Arabic name: سُورَةُ المُزَّمِّلِ
Surah English name: Al-Muzzammil
Surah number: 73
Number of verses: 20
--------------------
Surah Arabic name: سُورَةُ المُدَّثِّرِ
Surah English name: Al-Muddaththir
Surah number: 74
Number of verses: 56
--------------------
Surah Arabic name: سُورَةُ القِيَامَةِ
Surah English name: Al-Qiyaama
Surah number: 75
Number of verses: 40
--------------------
Surah Arabic name: سُورَةُ الإِنسَانِ
Surah English name: Al-Insaan
Surah number: 76
Number of verses: 31
--------------------
Surah Arabic name: سُورَةُ المُرۡسَلَاتِ
Surah English name: Al-Mursalaat
Surah number: 77
Number of verses: 50
--------------------
Surah Arabic name: سُورَةُ النَّبَإِ
Surah English name: An-Naba
Surah number: 78
Number of verses: 40
--------------------
Surah Arabic name: سُورَةُ النَّازِعَاتِ
Surah English name: An-Naazi'aat
Surah number: 79
Number of verses: 46
--------------------
Surah Arabic name: سُورَةُ عَبَسَ
Surah English name: Abasa
Surah number: 80
Number of verses: 42
--------------------
Surah Arabic name: سُورَةُ التَّكۡوِيرِ
Surah English name: At-Takwir
Surah number: 81
Number of verses: 29
--------------------
Surah Arabic name: سُورَةُ الانفِطَارِ
Surah English name: Al-Infitaar
Surah number: 82
Number of verses: 19
--------------------
Surah Arabic name: سُورَةُ المُطَفِّفِينَ
Surah English name: Al-Mutaffifin
Surah number: 83
Number of verses: 36
--------------------
Surah Arabic name: سُورَةُ الانشِقَاقِ
Surah English name: Al-Inshiqaaq
Surah number: 84
Number of verses: 25
--------------------
Surah Arabic name: سُورَةُ البُرُوجِ
Surah English name: Al-Burooj
Surah number: 85
Number of verses: 22
--------------------
Surah Arabic name: سُورَةُ الطَّارِقِ
Surah English name: At-Taariq
Surah number: 86
Number of verses: 17
--------------------
Surah Arabic name: سُورَةُ الأَعۡلَىٰ
Surah English name: Al-A'laa
Surah number: 87
Number of verses: 19
--------------------
Surah Arabic name: سُورَةُ الغَاشِيَةِ
Surah English name: Al-Ghaashiya
Surah number: 88
Number of verses: 26
--------------------
Surah Arabic name: سُورَةُ الفَجۡرِ
Surah English name: Al-Fajr
Surah number: 89
Number of verses: 30
--------------------
Surah Arabic name: سُورَةُ البَلَدِ
Surah English name: Al-Balad
Surah number: 90
Number of verses: 20
--------------------
Surah Arabic name: سُورَةُ الشَّمۡسِ
Surah English name: Ash-Shams
Surah number: 91
Number of verses: 15
--------------------
Surah Arabic name: سُورَةُ اللَّيۡلِ
Surah English name: Al-Lail
Surah number: 92
Number of verses: 21
--------------------
Surah Arabic name: سُورَةُ الضُّحَىٰ
Surah English name: Ad-Dhuhaa
Surah number: 93
Number of verses: 11
--------------------
Surah Arabic name: سُورَةُ الشَّرۡحِ
Surah English name: Ash-Sharh
Surah number: 94
Number of verses: 8
--------------------
Surah Arabic name: سُورَةُ التِّينِ
Surah English name: At-Tin
Surah number: 95
Number of verses: 8
--------------------
Surah Arabic name: سُورَةُ العَلَقِ
Surah English name: Al-Alaq
Surah number: 96
Number of verses: 19
--------------------
Surah Arabic name: سُورَةُ القَدۡرِ
Surah English name: Al-Qadr
Surah number: 97
Number of verses: 5
--------------------
Surah Arabic name: سُورَةُ البَيِّنَةِ
Surah English name: Al-Bayyina
Surah number: 98
Number of verses: 8
--------------------
Surah Arabic name: سُورَةُ الزَّلۡزَلَةِ
Surah English name: Az-Zalzala
Surah number: 99
Number of verses: 8
--------------------
Surah Arabic name: سُورَةُ العَادِيَاتِ
Surah English name: Al-Aadiyaat
Surah number: 100
Number of verses: 11
--------------------
Surah Arabic name: سُورَةُ القَارِعَةِ
Surah English name: Al-Qaari'a
Surah number: 101
Number of verses: 11
--------------------
Surah Arabic name: سُورَةُ التَّكَاثُرِ
Surah English name: At-Takaathur
Surah number: 102
Number of verses: 8
--------------------
Surah Arabic name: سُورَةُ العَصۡرِ
Surah English name: Al-Asr
Surah number: 103
Number of verses: 3
--------------------
Surah Arabic name: سُورَةُ الهُمَزَةِ
Surah English name: Al-Humaza
Surah number: 104
Number of verses: 9
--------------------
Surah Arabic name: سُورَةُ الفِيلِ
Surah English name: Al-Fil
Surah number: 105
Number of verses: 5
--------------------
Surah Arabic name: سُورَةُ قُرَيۡشٍ
Surah English name: Quraish
Surah number: 106
Number of verses: 4
--------------------
Surah Arabic name: سُورَةُ المَاعُونِ
Surah English name: Al-Maa'un
Surah number: 107
Number of verses: 7
--------------------
Surah Arabic name: سُورَةُ الكَوۡثَرِ
Surah English name: Al-Kawthar
Surah number: 108
Number of verses: 3
--------------------
Surah Arabic name: سُورَةُ الكَافِرُونَ
Surah English name: Al-Kaafiroon
Surah number: 109
Number of verses: 6
--------------------
Surah Arabic name: سُورَةُ النَّصۡرِ
Surah English name: An-Nasr
Surah number: 110
Number of verses: 3
--------------------
Surah Arabic name: سُورَةُ المَسَدِ
Surah English name: Al-Masad
Surah number: 111
Number of verses: 5
--------------------
Surah Arabic name: سُورَةُ الإِخۡلَاصِ
Surah English name: Al-Ikhlaas
Surah number: 112
Number of verses: 4
--------------------
Surah Arabic name: سُورَةُ الفَلَقِ
Surah English name: Al-Falaq
Surah number: 113
Number of verses: 5
--------------------
Surah Arabic name: سُورَةُ النَّاسِ
Surah English name: An-Naas
Surah number: 114
Number of verses: 6
--------------------
"""

available_languages = Literal[
"ar",
"am",
"az",
"ber",
"bn",
"cs",
"ce",
"de",
"dv",
"en",
"es",
"fa",
"fr",
"ha",
"hi",
"id",
"it",
"ja",
"ko",
"ku",
"ml",
"nl",
"no",
"pl",
"ps",
"pt",
"ro",
"ru",
"sd",
"so",
"sq",
"sv",
"sw",
"ta",
"tg",
"th",
"tr",
"tt",
"ug",
"ur",
"uz"
]
