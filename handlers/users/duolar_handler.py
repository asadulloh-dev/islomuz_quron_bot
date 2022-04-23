from filters import IsPrivate
from keyboards.default.duolar_keyboard import duolar
from loader import dp
from aiogram.dispatcher.filters.builtin import Command

from aiogram.types import Message


@dp.message_handler(text="🤲 Duo va zikrlar")
async def duola(mes: Message):
    text = """<b>Rosululloh ﷺ oʻqib yurgan duolar.

Ibn Masʼuddan (r.a.) rivoyat qilinadi. Rasululloh sollallohu alayhi vasallam: «Kimki

أسْتَغْفِرُ اللهَ العَظِيمَ الَّذِي لاَ إلَهَ إلاَّ هُوَ، الحَيُّ القَيُّومُ، وَأتُوبُ إلَيهِ

 «Astagʻfirullohallaziy la ilaha illa huval hayyul qayyum va atuvbu ilayhi»,
 deb aytsa, (Alloh) urushdan qochgandagi gunohini ham kechirib yuboradi», dedilar.</b>"""

    await mes.answer(text, reply_markup=duolar)


@dp.message_handler(text="Tongi va kechki zikrlar")
async def tongiz(mes: Message):
    text = """
<b>
Abu Hurayra roziyallohu anhudan rivoyat qilinadi:

Rasululloh sollallohu alayhi vasallam tong otganida:

اللهُمَّ بِكَ أَصْبَحْنَا وَبِكَ أَمْسَيْنَا وَبِكَ نَحْيَا وَبِكَ نَمُوتُ وَإِلَيْكَ النُّشُورُ 

«Allohumma bika asbahnaa va bika amsaynaa va bika nahyaa va bika namuutu va ilaykan nushuur»  der edilar.

Ma’nosi: Allohim, Sening noming ila tong ottirdik, Sening noming ila kech kirgizdik. Sening noming ila tirilamiz va Sening noming ila o‘lamiz. Va Senga qaytajakmiz.

Kech kirganida esa:

اللهُمَّ بِكَ أَمْسَيْنَا وَبِكَ أَصْبَحْنَا وَبِكَ نَحْيَا وَبِكَ نَمُوتُ وَإِلَيْكَ الْمَصِير 

«Allohumma bika amsaynaa va bika nahyaa va bika namuutu va ilaykal masiyr».

(“Allohim, Sening noming ila kech kirgizdik. Sening noming ila tirilamiz va Sening noming ila vafot etamiz. Va Senga qaytajakmiz”), deb aytar edilar.

Abu Dovud, Termiziy va Ibn Mojalar rivoyati.



Abdulloh ibn G‘annom roziyallohu anhudan rivoyat qilinadi: 

Rasululloh sollallohu alayhi vasallam: «Kim tong otganida:

اللهُمَّ مَا أَصْبَحَ بِي مِنْ نِعْمَةٍ، فَمِنْكَ وَحْدَكَ لاَ شَرِيكَ لَكَ، فَلَكَ الْحَمْدُ وَلَكَ الشُّكْرُ 

«Allohumma maa asbaha biy min ni’matin faminka vahdaka laa shariyka lak, falakal hamdu va lakash shukr», desa, kunduzning shukrini ado qilibdi. Kim shu duoni kech kirganida aytsa, kechaning shukrini ado etibdi», dedilar.

Ma’nosi: Allohim, men bilan tong ottirgan ne’matlar Sen tomondandir. Sen yakkayu yolg‘izdirsan, Sening sheriging yo‘q. Senga hamd va shukrlar bo‘lsin.

Abu Dovud rivoyatlari.

اللهُمَّ مَا أَمْسَى بِي مِنْ نِعْمَةٍ فَمِنْكَ وَحْدَكَ، لاَ شَرِيكَ لَكَ، فَلَكَ الْحَمْدُ وَلَكَ الشُّكْرُ  

Allohumma maa amsaa biy min ni’matin faminka vahdaka laa shariyka lak, lakal hamdu va lakash shukr»

Ma’nosi: Allohim, men bilan kech kirgizgan ne’matlar Sen tomondandir. Sen yakkayu yolg‘izdirsan, Sening sheriging yo‘q. Senga hamd va shukrlar bo‘lsin.

Batafsil: https://islom.uz/maqola/13522
👉 Zikrlar davomi: /zikr2

@islomuz_quron_bot
</b>"""
    await mes.answer(text)


@dp.message_handler(Command('zikr2'), IsPrivate())
async def zikr2(mes: Message):
    text = """
<b>
Ummul moʻminiyn Juvayriya roziyallohu anhodan rivoyat qilinadi: 

«Rasululloh sollallohu alayhi vasallam ertalab subh namozi paytida uning huzuridan chiqib ketdilar. U namoz oʻqiydigan xonasida edi. Soʻngra zuho namozini oʻqib boʻlib qaytib kelsalar, Juvayriya onamiz hali ham oʻtirgan edilar. Shunda Rasululloh sollallohu alayhi vasallam: «Chiqib ketganimdan beri shu holatda oʻtiribsanmi?» deb soʻradilar. Onamiz roziyallohu anho:  «Ha», deya javob berdilar. «Men sendan keyin toʻrtta kalimani uch martadan aytdim, agar ular tarozida oʻlchansa, sen bugun aytgan narsalardan ogʻir keladi, – dedilar Rasululloh sollallohu alayhi vasallam. – Ular:

سُبْحَانَ اللهِ وَبِحَمْدِهِ عَدَدَ خَلْقِهِ، وَرِضَى نَفْسِهِ، وَزِنَةَ عَرْشِهِ وَمِدَادَ كَلِمَاتِهِ مرات 

«Subhaanallohi va bihamdihi ʼadada xolqihi va ridoo nafsihi va zinata ʼarshihi va midaada kalimaatihi».

Maʼnosi: “Yaratganlarining adadicha, nafsi rozi boʻlgunicha, arshning vaznicha, kalimalarning uzunligicha Allohga hamd aytaman va Uni poklayman.

Imom Muslim rivoyatlari.

 

Abu Ayyub Ansoriy roziyallohu anhudan rivoyat qilinadi:

«Rasululloh sollallohu alayhi vasallam: «Kim:

لاَ إِلَهَ إِلاَّ اللهُ وَحْدَهُ لاَ شَرِيكَ لَهُ، لَهُ الْمُلْكُ وَلَهُ الْحَمْدُ وَهُوَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ 

«Laa ilaaha illallohu vahdahu laa shariyka lahu, lahul mulku va lahul hamdu va huva ʼalaa kulli shay`in qodiyr», deb oʻn marta aytsa, Ismoil zurriyotidan toʻrt kishini ozod qilgandek boʻladi», dedilar».

Maʼnosi: “Allohdan boshqa iloh yoʻq, U yolgʻiz, Uning sherigi ham yoʻq, butun mulk Uniki, hamd ham Unga xos va U har bir narsaga qodirdir.

Imom Buxoriy va Muslim rivoyatlari.

 

Abu Said Xudriy roziyallohu anhudan rivoyat qilinadi:

Rasululloh sollallohu alayhi vasallam: «Kim:

رَضِيتُ بِاللهِ رَبًّا، وَبِالإِسْلاَمِ دِينًا وَبِمُحَمَّدٍ صلى الله عليه وسلم رَسُولاً 

«Rodiytu billaahi robban va bil islaami diynan va bimuhammadin sollalloohu alayhi vasallama rosulaa», desa, unga jannat vojib boʻladi», dedilar.

Maʼnosi: “Allohni rabbim deb, Islomni dinim deb, Muhammad alayhissalomni rasul deb rozi boʻldim.

Abu Dovud rivoyat qilganlar.

 

Abdulloh ibn Hubayb roziyallohu anhudan rivoyat qilinadi :

«Biz zulmatli yomgʻirli kechada Rasululloh sollallohu alayhi vasallam namoz oʻqib berishlari uchun u zotni axtarib koʻchaga chiqdik. U zotni topganimizda, «Ayt», dedilar. Men hech bir narsa ayta olmadim. Soʻngra yana: «Ayt», dedilar. Men hech narsa ayta olmadim. Soʻngra yana: «Ayt», dedilar. Men: «Ey Rasululloh, nimani aytaman?» dedim. Shunda Rasululloh sollallohu alayhi vasallam:

قُلْ هُوَ اللهُ أحَدٌ... قُلْ أعُوذُ بِرَبِّ الفَلَقِ... قُلْ أعُوذُ بِرَبِّ النَّاسِ...  

«Qul huvalloohu ahad», «Qul aʼuuzu birobbil falaq», «Qul aʼuuzu birobbinnaas» suralarini kechki payt va ertalab uch martadan aytsang, senga har bir narsada kifoya qiladi», dedilar».

Abu Dovud, Termiziy, Nasaiylar rivoyati.

👉Zikrlar davomi: /zikr3

@islomuz_quron_bot
</b>"""
    await mes.answer(text)


@dp.message_handler(Command('zikr3'), IsPrivate())
async def zikr3(mes: Message):
    text="""
<b>
Shaddod ibn Avs roziyallohu anhudan rivoyat qilinadi : 

Rasululloh sollallohu alayhi vasallam: «Kim sayyidul istigʻfor:

اللهُمَّ أَنْتَ رَبِّي، لاَ إِلَهَ إِلاَّ أَنْتَ خَلَقْتَنِي، وَأَنَا عَبْدُكَ، وَأَنَا عَلَى عَهْدِكَ وَوَعْدِكَ مَا اسْتَطَعْتُ، أَعُوذُ بِكَ مِنْ شَرِّ مَا صَنَعْتُ، أَبُوءُ لَكَ بِنِعْمَتِكَ عَلَيَّ وَأَبُوءُ بِذَنْبِي فَاغْفِرْ لِي فَإِنَّهُ لاَ يَغْفِرُ الذُّنُوبَ إِلاَّ أَنْتَ 

«Allohumma anta robbiy laa ilaaha illa anta xolaqtaniy va anaa ʼabduka va anaa ʼalaa ʼahdika va vaʼdika mastatoʼtu aʼuuzu bika min sharri maa sonaʼtu, abuu`u laka biniʼmatika ʼalayya va abuu`u bizambiy fagʻfirliy fainnahuu la yagʻfiruz zunuba illaa anta»ni  kechki payt aytib, tong otgunicha vafot etsa, jannatga kiradi. Kim tongda aytib, shu kuni vafot etsa, unda ham jannatga kiradi», dedilar.

Maʼnosi: “Allohim, Sen parvardigorimsan, Sendan boshqa iloh yoʻq. Meni xalq qilding va men Sening qulingman. Men Senga bergan vaʼdamda va Senga bergan ahdimda qodir boʻlganimcha turibman. Qilgan narsalarimning yomonidan Sening noming bilan panoh tilayman. Menga ato qilgan neʼmatlaringga iqror boʻldim. Va yana gunohlarimga ham iqror boʻldim. Mening gunohlarimni kechir. Chunki Sendan boshqasi gunohlarni kechira olmaydi.

Imom Buxoriy rivoyatlari.

 

Abu Hurayra roziyallohu anhu aytadilar:

«Rasululloh sollallohu alayhi vasallam huzurlariga bir kishi kelib: «Ey Rasululloh, kecha meni chayon chaqib oldi», dedi. Shunda Nabiy sollallohu alayhi vasallam: «Kech kirganida:

أَعُوذُ بِكَلِمَاتِ اللهِ التَّامَّاتِ مِنْ شَرِّ مَا خَلَقَ  

«Aʼuzu bikalimatillahit tammati min sharri ma xolaq», desang, senga hech narsa zarar bermaydi», dedilar.

Maʼnosi: “Allohning hamma kalimalari bilan U yaratgan narsalarning yomonligidan panoh tilayman.

Imom Muslim rivoyatlari.


Usmon ibn Affon  roziyallohu anhudan rivoyat qilinadi : 

Rasululloh sollallohu alayhi vasallam: «Biror bir banda har tongda va tunda:

بِاسْمِ اللهِ الَّذِي لاَ يَضُرُّ مَعَ اسْمِهِ شَيْءٌ فِي الأَرْضِ وَلاَ فِي السَّمَاء وَهُوَ السَّمِيعُ العَلِيمُ

«Bismillaahillaziy la yadurru maʼasmihii shay`un fil ardi va laa fis samai va huvas samiyʼul ʼaliym», deb uch marta aytsa, unga biror narsa zarar bermaydi», dedilar.

Maʼnosi: Shunday Allohning ismi bilan boshlaymanki, Uning ismi tufayli yeru osmonda biror narsa zarar bera olmaydi. U eshituvchi va biluvchi Zotdir.

Abu Dovud va Termiziy rivoyatlari.

 

Abdurahmon ibn Abu Bakra otalariga: «Ey otajon, har tongda uch marta va kechqurun uch marta:

اللهُمَّ عَافِنِي فِي بَدَنِي، اللهُمَّ عَافِنِي فِي سَمْعِي، اللهُمَّ عَافِنِي فِي بَصَرِي، لا إلَهَ إلاَّ أنْتَ. اللهُمَّ  إِنِّي أَعُوذُ بِكَ مِنَ الكُفْرِ وَالفَقْرِ، اللهُمَّ إِنِّي أَعُوذُ بِكَ مِنْ عَذَابِ القَبْرِ لاَ إِلَهَ إِلاَّ أَنْتَ

«Allohumma ʼaafiniy fiy badaniy, Allohumma ʼaafiniy fiy samʼiy, Allohumma ʼaafiniy fiy basoriy, laa ilaaha illa anta. Allohumma inniy aʼuuzu bika minal kufri val faqri, Allohumma inniy aʼuuzu bika min ʼazabil qobr, laa ilaaha illaa anta» deyayotganingizni eshitaman», dedilar. Abu Bakra roziyallohu anhudan rivoyat qilinadi: «Men Rasululloh sollallohu alayhi vasallamning shunday duo qilganlarini eshitganman va men u zotning sunnatlariga amal qilishni yaxshi koʻraman»,  deb javob berdilar.

(Maʼnosi: “Allohim, badanimni, qulogʻimni va koʻzimni ofiyatda qil. Ey Rabbim, Sening noming ila kufrdan, kambagʻallikdan va qabr azobidan panoh tilayman. Sendan boshqa iloh yoʻq”).

Abu Dovud rivoyatlari.

👉Davomi: /zikr4

@islomuz_quron_bot
</b>"""
    await mes.answer(text)


@dp.message_handler(Command('zikr4'), IsPrivate())
async def zikr4(mes: Message):
    text="""
<b>
Abu Molik Ashʼariy roziyallohu anhudan rivoyat qilinadi:

Rasululloh sollallohu alayhi vasallam: «Sizlardan biringiz tong otganida:

أَصْبَحْنَا وَأَصْبَحَ الْمُلْكُ للهِ رَبِّ العَالَمِينَ. اللهُمَّ أَسْأَلُكَ خَيْرَ هَذَا اليَوْمِ فَتْحَهُ وَنَصْرَهُ وَنُورَهُ وَبَرَكَتَهُ وَهُدَاهُ وَأَعُوذُ بِكَ مِنْ شَرِّ مَا فِيهِ وَشَرِّ مَا بَعْدَهُ

أمْسَينَا وَأَمْسَى الْمُلْكُ للهِ رَبِّ العَالَمِينَ. اللهُمَّ أَسْأَلُكَ خَيْرَ هَذِهِ اللَّيلَةِ، فَتْحَهُ وَنَصْرَهُ وَنُورَهُ وَبَرَكَتَهُ وَهُدَاهُ وَأَعُوذُ بِكَ مِنْ شَرِّ مَا فِيهَا، وَشَرِّ مَا بَعْدَهَا

«Asbahnaa va asbahal mulku lillaahi robbil ʼaalamiyn. Allohumma as`aluka xoyra haazal yavmi fathahu va nasrohu va nuurohu va barokatahu va hudaahu va aʼuuzu bika min sharri maa fiyhi va sharri maa baʼdah», deb aytsin. Soʻngra kech kirganida ham xuddi shunday desin», dedilar.

Maʼnosi: “Biz ham, mulk ham olamlar parvardigori Allohniki boʻlgan holda tong ottirdik. Ey Rabbim, bu kunning yaxshisini, fath boʻlishini, gʻalabasini, nurini, barakasini, hidoyatini soʻrayman. Va Sendan bu kunning va bu kundan keyingisining yomonligidan panoh tilayman.

Abu Dovud rivoyatlari.

 

Anas roziyallohu anhudan rivoyat qilinadi:

Rasululloh sollallohu alayhi vasallam: «Kim tong otganida yoki kech kirganida:

اللهُمَّ إنِّي أصْبَحْتُ أُشْهِدُكَ، وَأُشْهِدُ حَمَلَةَ عَرْشِكَ، وَمَلاَئِكَتِكَ وَجَمِيعَ خَلْقِكَ، أَنَّكَ أنْتَ اللهُ لاَ إلَهَ إلاَّ أنْتَ، وَحْدَكَ لاَ شَرِيكَ لَكَ، وَأنَّ مُحَمَّدًا عَبْدُكَ وَرَسُولُكَ

اللهُمَّ إنِّي أمْسَيتُ أُشْهِدُكَ، وَأشْهِدُ حَمَلَةَ عَرْشِكَ، وَمَلاَئِكَتِكَ وَجَمِيعَ خَلْقِكَ، أنَّكَ أنْتَ اللهُ لاَ إلَهَ إلاَّ أنْتَ، وَحْدَكَ لاَ شَرِيكَ لَكَ، وَأنَّ مُحَمَّدًا عَبْدُكَ وَرَسُولُكَ

«Allohumma inniy asbahtu ushhiduka va ushhidu hamalata ʼarshika va malaaikatika va jamiyʼa xolqik, annaka antalloohu laa ilaaha illa anta vahdaka laa shariyka laka va anna Muhammadan ʼabduka va rosuuluk», deb aytsa, Alloh taolo tanasining toʻrtdan birini doʻzaxdan xalos qiladi. Kim shuni ikki marta aytsa, Alloh taolo uning yarmini doʻzaxdan xalos qiladi. Kim uch marta aytsa, Alloh taolo uning toʻrtdan uch qismini doʻzaxdan xalos etadi. Kim toʻrt marta aytsa, Alloh taolo uni butunlay doʻzaxdan xalos qiladi», dedilar.

Maʼnosi: Allohim, albatta, men tong ottirdim. Seni hamda arshingni koʻtaruvchi farishtalaringni va hamma xalq qilgan narsalaringni guvoh qilib aytamanki, Sendan boshqa iloh yoʻq, Muhammad sollallohu alayhi vasallam Sening bandang va rasulingdir.

Abu Dovud rivoyatlari.

 

Abu Hurayra roziyallohu anhudan rivoyat qilinadi : 

Abu Bakr Siddiq roziyallohu anhu «Ey Rasululloh, menga biror kalima oʻrgating, men uni ertalab va kechqurun aytib yuray», deganlarida, Rasululloh sollallohu alayhi vasallam:

اللهُمَّ فَاطِرَ السَّمَاوَاتِ وَالأَرْضِ عَالِمَ الغَيْبِ وَالشَّهَادَةِ، رَبَّ كُلِّ شَيْءٍ وَمَلِيكَهُ، أَشْهَدُ أَنْ لاَ إِلَهَ إِلاَّ أَنْتَ، أَعُوذُ بِكَ مِنْ شَرِّ نَفْسِي، وَشَرِّ الشَّيْطَانِ وَشِرْكِهِ

«Allohumma fatiros samavati val arzi ʼalimal gʻoybi vash shahadati robba kulli shay`in va maliykah, Ashhadu alla ilaha illa anta, aʼuzu bika min sharri nafsiy va sharrish shaytoni va shirkih», deb erta tongda, kech kirganda va joyingga yonboshlab yotganingda ayt», dedilar.

Maʼnosi: “Ey yeru osmonni bor qilgan Rabbim, ey gʻoibni va shohidni biluvchi Rabbim, Sen har bir narsaning parvardigori va podshohidirsan. Guvohlik beramanki, Sendan boshqa iloh yoʻq. Nafsimning yomonligidan, shaytonning yomonligiyu shirkidan Sening noming ila panoh tilayman.

Abu Dovud va Termiziylar rivoyati.

 

Abu Hurayra roziyallohu anhudan rivoyat qilinadi:

Rasululloh sollallohu alayhi vasallam: «Kim ertalab yoki kechqurun:

سُبْحَانَ اللهِ وَبِحَمْدِهِ

سُبْحَانَ اللهِ وَبِحَمْدِهِ سُبْحَانَ اللهِ العَظِيمِ

«Subhaanallohi va bihamdihi», (Allohga hamd aytish bilan Uni aybu nuqsonlardan poklab yod etaman), deb yuz marta aytsa, qiyomat kuni biror kishi undan afzal boʻlmaydi. Faqat ana shu kishi aytganidek yoki undan oshirib aytsagina, boʻlishi mumkin», dedilar.

Imom Muslim rivoyatlari.

👉Davomi: /zikr5

@islomuz_quron_bot
</b>    
"""
    await mes.answer(text)


@dp.message_handler(Command('zikr5'), IsPrivate())
async def zikr5(mes: Message):
    text="""
<b>
Sizning matningiz:

Abu Hurayra roziyallohu anhudan rivoyat qilinadi : 

«Rasululloh sollallohu alayhi vasallam:

سُبْحَانَ اللهِ وَالْحَمْدُ للهِ وَلاَ إِلَهَ إِلاَّ اللهُ وَاللهُ أَكْبَرُ

«Subhaanallohi valhamdu lillaahi va laa ilaaha illalloohu valloohu  akbar», deyishim men uchun quyosh chiqib, nur sochganidan yaxshiroqdir», dedilar».

Imom Muslim rivoyatlari.

 

Anas roziyallohu anhudan rivoyat qilinadi:

Rasululloh alayhissalom Fotima roziyallohu anhoga: «Vasiyat qilgan narsamni eshitishdan seni nima toʻsadi? Har tong va kechqurun:

يَا حَيُّ يَا قَيُّومُ، بِرَحْمَتِكَ أَسْتَغِيثُ، أَصْلِحْ لِي شَأْنِي كُلَّهُ، وَلاَ تَكِلْنِي إِلَى نَفْسِي طَرْفَةَ عَيْنٍ

«Yaa hayyu yaa qoyyuumu birohmatika astagʻiysu aslih liy sha`niy kullahu va laa takilniy ilaa nafsiy torfata ʼayn», deb ayt», dedilar.

Maʼnosi: Ey hay-tirik va qayyum sifatiga ega boʻlgan Zot, Sendan yordam soʻrayman. Shaʼnimni har bir narsada isloh et va koʻz yumib ochgunchalik muddat ham oʻz holimga tashlab qoʻyma.

Ibn Sunniy rivoyatlari.

 

Abu Dardo roziyallohu anhudan rivoyat qilinadi:

Rasululloh sollallohu alayhi vasallam: «Kim har kuni tong otganida va kech kirganida:

حَسْبِيَ اللهُ لاَ إِلَهَ إِلاَّ هُوَ عَلَيْهِ تَوَكَّلْتُ وَهُوَ رَبُّ العَرْشِ العَظِيمِ 

«Hasbiyallohu la ilaha illa huva ʼalayhi tavakkaltu va huva robbul ʼarshil ʼaziym» (Alloh menga kifoya qiladi. Undan boshqa iloh yoʻq. Unga tavakkal qildim. U ulugʻ arshning Rabbidir), deb yetti marta aytsa, uning dunyo va oxiratdagi muhim ishlarida Allohning Oʻzi kifoya qiladi», dedilar.

Ibn Sunniy rivoyatlari.

 

Maʼqal ibn Yasor roziyallohu anhudan rivoyat qilinadi:

Rasululloh sollallohu alayhi vasallam: «Tong otganida kim uch marta: «Aʼuzu billahis samiyʼul ʼaliym minash shaytonir rojiym», deb Hashr surasidan uch oyat oʻqisa, Alloh taolo unga kech kirgunicha salovot aytib turadigan yetmish ming farishtani vakil qilib qoʻyadi. Agar vafot etsa, shahid ketadi», dedilar.

Maʼnosi: “Eshituvchi va biluvchi Allohning nomi ila laʼnatlangan shaytondan panoh tilayman.

Termiziy va Ibn Sunniy zaif isnod bilan rivoyat qilishgan.

 

Ibn Umar roziyallohu anhu aytadilar:

«Rasululloh sollallohu alayhi vasallam quyidagi duolarni kech kirganida va tong otganida hech tark qilmas edilar:

اللَّهُمَّ إنِّي اسْألُكَ العَافِيَةَ فِي الدُّنْيَا وَالآخِرَةِ، اللَّهُمَّ إنِّي اسْألُكَ العَفْوَ وَالعَافِيَةَ فِي دِيْنِي وَدُنْيَايَ وَأهْلِي وَمَالِي، اللَّهُمَّ اسْتُرْ عَورَاتِي وَآمِنْ رَوْعَاتِي، اللَّهُمَّ احْفَظْنِي مِنْ بَيْنِ يَدَيَّ وَمِنْ خَلْفِي وَعَنْ يَمِينِي وَعَنْ شِمَالِي وَمِنْ فَوقِي وَأعُوذُ بِعَظَمَتِكَ أَنْ أُغْتَالَ مِنْ تَحْتِي

«Allohumma inniy as`alukal ʼafiyata fiddunya val aaxiroh. Allohumma inniy as`alukal ʼafva val ʼafiyata fiy diyniy va dunyaya va ahliy va maaliy. Allohummastur ʼavrootiy va aamin ravʼatiy. Allohummahfazniy min bayni yadayya va min xolfiy va ʼan yamiyniy va ʼan shimaaliy va min favqiy va aʼuzu biʼazomatika an ugʻtaala min tahtiy».

Maʼnosi: “Allohim, men Sendan dunyo va oxiratda ofiyat soʻrayman. Ey Rabbim, dinimda va dunyoimda, ahlimda va molimda avf va ofiyat soʻrayman. Ey Rabbim, avratimni bekit, xavflarimni omonlikka aylantir. Ey Allohim, meni oldimdan, orqamdan, oʻng tomonimdan, chap tomonimdan, ustimdan saqlagin. Ey Rabbim, ostimdan halok qilishingdan Sening azamating ila panoh tilayman.

Abu Dovud, Nasaiy va Ibn Mojalar rivoyati.

 Ummu Salama roziyallohu anho onamizdan rivoyat qilinadi:

Rasululloh sollallohu alayhi vasallam tong otsa:

اللَّهُمَّ إنِّي اسْأَلُكَ عِلْمًا نَافِعًا وَرِزْقًا طَيِّبًا وَعَمَلاً مُتَقَبَّلاً

«Allohumma inniy as`aluka ʼilman nafiʼan va rizqon toyyiban va ʼamalan mutaqobbala», deb aytar edilar.

Maʼnosi: “Allohim, Sendan foydali ilm, pokiza rizq, qabul boʻladigan amal soʻrayman.

Ibn Moja va Ibn Sunniy rivoyatlari.

Manba: islom.uz

@islomuz_quron_bot
</b>  
"""
    await mes.answer(text)


@dp.message_handler(text="Qur'onda kelgan duolar")
async def quroniyduolar(mes: Message):
    text="""
<b>
«Alhamdulillaahi vahdahu vassolaatu vassalaamu ’alaa Rosulillaah»



رَبَّنَا ظَلَمْنَا أَنفُسَنَا وَإِن لَّمْ تَغْفِرْ لَنَا وَتَرْحَمْنَا لَنَكُونَنَّ مِنَ الْخَاسِرِينَ

Robbanaa zolamnaa anfusanaa va il-lam tag‘fir lanaa va tarhamnaa la-nakunanna minal-xosiriyn.

Ma’nosi: «Ey Robbimiz, biz o‘zimizga zulm qildik. Agar Sen bizni mag‘firat qilmasang va bizga rahim qilmasang, albatta, ziyon ko‘rganlardan bo‘lamiz».(“A’rof” surasi, 23-oyat)

•┈•┈•┈•┈•❁✿❁•┈•┈•┈•┈•

‎رَبَّنَا آتِنَا فِي الدُّنْيَا حَسَنَةً وَفِي الآخِرَةِ حَسَنَةً وَقِنَا عَذَابَ النَّارِ

Robbanaa aatinaa fiddunya hasanatan va fil aaxiroti hasanatan va qinaa azaban-naar.

Ma’nosi: «Rabbimiz, bizga dunyoda ham yaxshilik ato etgin, oxiratda ham ‌‎yaxshilik (ato etgin) va bizni do‘zax azobidan asragin».
(“Baqara” surasi, 201-oyat).

•┈•┈•┈•┈•❁✿❁•┈•┈•┈•┈•

ربنا لا تُؤَاخِذْنَا إِن نَّسِينَا أَوْ أَخْطَأْنَا رَبَّنَا وَلاَ تَحْمِلْ عَلَيْنَا إِصْرًا كَمَا حَمَلْتَهُ عَلَى الَّذِينَ مِن قَبْلِنَا رَبَّنَا وَلاَ تُحَمِّلْنَا مَا لاَ طَاقَةَ لَنَا بِهِ وَاعْفُ عَنَّا وَاغْفِرْ لَنَا وَارْحَمْنَا أَنتَ مَوْلاَنَا فَانصُرْنَا عَلَى الْقَوْمِ الْكَافِرِينَ

Robbanaa laa tu'axiznaa in nasiinaa av axto'naa, Robbanaa valaa tahmil ’alaynaa isron kamaa hamaltahuu ’alallaziyna min qoblinaa, Robbanaa valaa tuhammilnaa maa laa toqota lanaa bih, va’fu ’annaa vag‘firlanaa varhamnaa anta mavlaanaa fansurnaa ’ala-l-qovmil-kaafiriin. 

Ma’nosi: «Ey, Rabbimiz, agar unutsak yoki xato qilsak, bizni javobgar etma! Ey, Rabbimiz, bizdan ilgari o‘tganlarning zimmasiga ortgan mashqqatni bizning zimmamizga ortma! Ey, Rabbimiz, toqatimiz yetmaydigan narsani bizga yuklab tashlama! Bizlarni afv et va kechir hamda bizlarga rahm qil! Sen bizning Xojamizsan. Bas, bizlarga kofirlar qavmi ustidan g‘oliblik ato et!». 
(“Baqara” surasi, 286-oyat)

•┈•┈•┈•┈•❁✿❁•┈•┈•┈•┈•

رَبَّنَا لَا تُزِغْ قُلُوبَنَا بَعْدَ إِذْ هَدَيْتَنَا وَهَبْ لَنَا مِن لَّدُنكَ رَحْمَةً ۚ إِنَّكَ أَنتَ الْوَهَّابُ 

Robbanaa laa tuzig‘ quluubanaa ba’da iz hadaytanaa va hablanaa min ladunka rohmatan, innaka anta-l-vahhaab. 

Ma’nosi: «Ey Robbimiz, bizni hidoyat qilganingdan so‘ng qalblarimizni og‘dirmagin va bizga O‘z huzuringdan rahmat ato qilgin. Albatta Sening O‘zing ko‘plab ato qiluvchisan».
(«Oli Imron» surasi, 8-oyat)

•┈•┈•┈•┈•❁✿❁•┈•┈•┈•┈•

رَبِّ لَا تَذَرْنِي فَرْدًا وَأَنتَ خَيْرُ الْوَارِثِينَ

Robbi laa tazarniy fardan va anta xoyru-l-vaarisiyn

Ma’nosi: «Ey Robbim, meni yolg‘iz tashlab qo‘yma, (menga O‘z dargohingdan bir merosxo‘r farzand ato et) Sen, O‘zing vorislarning eng yaxshisisan».
(“Anbiyo” surasi, 89-oyat)

حَسْبِيَ اللَّهُ لا إِلَـهَ إِلاَّ هُوَ عَلَيْهِ تَوَكَّلْتُ وَهُوَ رَبُّ الْعَرْشِ الْعَظِيمِ

Hasbiyallohu laa ilaaha illa huva ’alayhi tavakkaltu va huva robbu-l-’arshil-l-’aziim.  

Ma’nosi: «Menga Alloh kifoyadir. Undan o‘zga iloh yo‘qdir. Unga tavakkul qildim. U buyuk Arshning parvardigoridir!»  
(“Tavba” surasi, 129-oyat).

•┈•┈•┈•┈•❁✿❁•┈•┈•┈•┈•

رَبِّ هَبْ لِي مِن لَّدُنكَ ذُرِّيَّةً طَيِّبَةً ۖ إِنَّكَ سَمِيعُ الدُّعَاءِ 

Robbi habliy min ladunka zurriyyatan toyyibatan innaka samii’u-d-du’aa'i. 

Ma’nosi: “Rabbim, menga (ham) o‘z huzurirgdan pok zurriyot ato et! Darhaqiqat, Sen duoni eshitguvchidirsan”. 
(«Oli Imron» surasi, 38-oyat)

•┈•┈•┈•┈•❁✿❁•┈•┈•┈•┈•

رَبَّنَا آمَنَّا فَاغْفِرْ لَنَا وَارْحَمْنَا وَأَنتَ خَيْرُ الرَّاحِمِينَ

Robbanaa aamannaa fag‘firlanaa varhamnaa va anta xoyrur-rohimiyn.

Ma’nosi: “Ey, Robbimiz! (o‘zingga) iymon keltirdik. Bas, bizlarni mag‘firat qilgin va bizlarga rahm ayla. Sen o‘zing rahm qiluvchilarning yaxshisidirsan”.
(“Mu’minun” surasi, 109-oyat)

Manba va batafsil: https://telegra.ph/ҚURON-VA-SUNNATDA-KELGAN-BAZI-DUOLAR-11-09

@islomuz_quron_bot
</b>"""
    text2="""
<b>
رَبَّنَا هَبْ لَنَا مِنْ أَزْوَاجِنَا وَذُرِّيَّاتِنَا قُرَّةَ أَعْيُنٍ وَاجْعَلْنَا لِلْمُتَّقِينَ إِمَامًا

Robbanaa hab lanaa min azvaajinaa va zurriyyaatinaa qurrota a’yuniv vaja’lnaa lil-muttaqiyna imaamaa. 

Ma’nosi: “Ey Robbimiz, O‘zing bizga ayollarimizdan va zurriyotlarimizdan ko‘zimiz quvonchini hadya etgin hamda bizlarni taqvodorlarga yetakchi qilgin”. 
(“Furqon” surasi, 74-oyat)

•┈•┈•┈•┈•❁✿❁•┈•┈•┈•┈•

رَبَّنَا اغْفِرْ لَنَا وَلِإِخْوَانِنَا الَّذِينَ سَبَقُونَا بِالْإِيمَانِ وَلَا تَجْعَلْ فِي قُلُوبِنَا غِلًّا لِّلَّذِينَ آمَنُوا رَبَّنَا إِنَّكَ رَءُوفٌ رَّحِيمٌ

Robbanag‘fir lanaa va liixvaaninallaziyna sabaquunaa bi-l-iymaani valaa taj’al fiy quluubinaa g‘illallillaziyna aamanuu Robbanaa innaka Rouufur-rohiym.

Ma’nosi: “Ey Robbimiz, bizlarni va iymonda bizdan ilgari bӯlgan birodarlarimizni mag‘firat qilgin hamda (barcha) mӯminlarga nisbatan dilimizda g‘illu-g‘ashlik (paydo) qilmagin. Ey Robbimiz, Sen albatta Rauff(ӯta mehribon va shafqatli) va Rohiym(Qiyomat kuni faqat mӯminlarga rahim qiluvchi) dursan”.
(“Hashr” surasi, 10-oyat)

•┈•┈•┈•┈•❁✿❁•┈•┈•┈•┈•

رَبَّنَا تَقَبَّلۡ مِنَّا  ؕ اِنَّكَ اَنۡتَ السَّمِيۡعُ الۡعَلِيۡمُ
‏وَتُبۡ عَلَيۡنَا ۚ اِنَّكَ اَنۡتَ التَّوَّابُ الرَّحِيۡمُ‏

Robbanaa taqobbal minnaa innaka antas-sami’ul-’aliym va tub ’alaynaa innaka antat-tavvaabur-rohiym.

Ma’nosi: «Ey Rabbimiz, bizdan (ushbu ishimizni) qabul et, albatta, Sen Eshituvchi va Biluvchi Zotsan»,... va tavbamizni qabul et. Albatta, Sen Tavvob (tavbalarni ko‘plab qabul etuvchi) rahmli Zotsan».
(“Baqara” surasi, 127-128 - oyatlar)

•┈•┈•┈•┈•❁✿❁•┈•┈•┈•┈•

رَبِّ اجْعَلْنِي مُقِيمَ الصَّلَاةِ وَمِن ذُرِّيَّتِي رَبَّنَا وَتَقَبَّلْ دُعَاءِ 

Robbij’alniy muqiima-s-solaati va min zurriyyatiy, Robbanaa va taqobbal du’aai. 

Ma’nosi: «Ey Rabbim! Meni va zurriyotimdan (ko‘p farzandlarimni) namozni barkamol ado etuvchi qilgin! Ey Rabbimiz! Duoimni qabul et»! 
(“Ibrohim” surasi, 40-oyat)

•┈•┈•┈•┈•❁✿❁•┈•┈•┈•┈•

‎رَبِّ أَوْزِعْنِي أَنْ أَشْكُرَ نِعْمَتَكَ الَّتِي أَنْعَمْتَ عَلَيَّ وَعَلَىٰ وَالِدَيَّ وَأَنْ أَعْمَلَ صَالِحًا تَرْضَاهُ وَأَصْلِحْ لِي فِي ذُرِّيَّتِي إِنِّي تُبْتُ إِلَيْكَ وَإِنِّي مِنَ الْمُسْلِمِينَ

Robbi avzi’niy an ashkuro ni’matakallatiy an’amta ’alayya va ’alaa vaalidayya va an a’mala solihan tarzohu va aslihliy fiy zurriyyatiy inniy tubtu ilayka va inniy minal muslimiyn.

Ma’nosi: «Ey, Rabbim! Menga va ota-onamga in’om etgan ne’matingga shukur qilishga va O‘zing rozi bo‘ladigan solih amalni qilishga meni muvaffaq etgin va men uchun zurriyotimni isloh et! Albatta, men Senga (gunohlarimdan) tavba qildim va albatta, men musulmonlardandirman.» 
(“Ahqof” surasi, 15-oyat)

•┈•┈•┈•┈•❁✿❁•┈•┈•┈•┈•

‎رَّبَّنَا عَلَيْكَ تَوَكَّلْنَا وَإِلَيْكَ أَنَبْنَا وَإِلَيْكَ الْمَصِيرُ

‎رَبَّنَا لَا تَجْعَلْنَا فِتْنَةً لِّلَّذِينَ كَفَرُوا وَاغْفِرْ لَنَا رَبَّنَا إِنَّكَ أَنتَ الْعَزِيزُ الْحَكِيمُ

Robbanaa ’alayka tavakkalnaa va ilayka anabnaa va ilayka-l-masiir. 

Robbanaa laa taj’alnaa fitnatan lillaziyna kafaruu vag‘firlanaa Robbanaa innaka antal-aziizu-l-hakiim.

Ma’nosi: “Ey, Rabbimiz! Sengagina tavakkul qildik, O‘zingga qaytdik va qaytishimiz ham faqat Sening huzuring saridir.

Ey, Rabbimiz! Bizni kofir bo‘lgan kimsalarga aldanuvchi qilib qo‘ymagin, bizni mag‘firat etgin! Ey, Rabbimiz! Albatta, Sen o‘zing Qudratli va Hikmatli (zot)dirsan!” 
(“Mumtahana” surasi, 4-5 oyatlar).

•┈•┈•┈•┈•❁✿❁•┈•┈•┈•┈•

‎رَبِّ اشْرَحْ لِي صَدْرِي وَيَسِّرْ لِي أَمْرِي وَاحْلُلْ عُقْدَةً مِّن لِّسَانِي يَفْقَهُوا قَوْلِي

Robbishrohliy sodriy. Va yassirliy amriy. Vahlul ’uqdatam millisaaniy. Yafqohuu qovliy.

Ma’nosi: «Ey Robbim, mening qalbimni keng qil. Mening ishimni oson qil. Tilimdagi tugunni yechgin. So‘zimni anglasinlar.»
(“Toho” surasi, 25-28 oyatlar).

رَبَّنَا اغْفِرْ لِي وَلِوَالِدَيَّ وَلِلْمُؤْمِنِينَ يَوْمَ يَقُومُ الْحِسَابُ

Robbanag‘firliy va livaalidayya va lilmu‘miniina yavma yaquumu-l-hisaab.

Manosi: “Ey, Rabbimiz! Hisob-kitob qilinadigan (qiyomat) kuni meni, ota-onamni va (barcha) mo‘minlarni mag‘firat qilgin!”
(“Ibrohim” surasi, 41-oyat.)

@islomuz_quron_bot
</b>"""
    await mes.answer(text)
    await mes.answer(text2)


@dp.message_handler(text="Sunnatda kelgan duolar")
async def duolar2(mes: Message):
    text="""
<b>
رَبَّنَا آمَنَّا فَاغْفِرْ لَنَا وَارْحَمْنَا وَأَنتَ خَيْرُ الرَّاحِمِينَ

Robbanaa aamannaa fag‘firlanaa varhamnaa va anta xoyrur-rohimiyn.

Ma’nosi: “Ey, Robbimiz! (o‘zingga) iymon keltirdik. Bas, bizlarni mag‘firat qilgin va bizlarga rahm ayla. Sen o‘zing rahm qiluvchilarning yaxshisidirsan”.
(“Mu’minun” surasi, 109-oyat)

•┈•┈•┈•┈•🌸🌺🌸•┈•┈•┈•┈•

اللَّهُمَّ إِنَّكَ عُفُوٌّ تُحِبُّ الْعَفْوَ فَاعْفُ عَنِّي

Allohumma innaka ’afuvvun, tuhibbul ’afva fa’fu ’anniy.

 Ma’nosi: «Allohim, Sen Afuvvsan, afv etishni yaxshi ko‘rasan. Meni afv et».
(Termiziy, Ibn Moja rivoyati)

•┈•┈•┈•┈•❁✿❁•┈•┈•┈•┈•

اللَّهُمَّ إنِّي أعُوذُ بِكَ مِنْ جَهْدِ الْبَلَاءِ، وَدَرَكِ الشَّقَاءِ، وَسُوءِ الْقَضَاءِ، وَشَمَاتَةِ الْأَعْدَاءِ

Allohumma inniy a’uuzu bika min jahdi-l-balaa’i va daroki-sh-shaqo’i va su’i-l-qodo’i va shamaatati-l-a’’daa’i. 

Ma’nosi: «Allohim, men Sendan qattiq sinovdan, ketma-ket keluvchi baxtsizlikdan, taqdir yomonligidan, dushmanlarning ichi qoraligi (ko‘rolmasliklardan) panoh tilayman».
(Buxoriy va Muslim rivoyati) 

•┈•┈•┈•┈•❁✿❁•┈•┈•┈•┈•

‏اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنْ فِتْنَةِ النَّارِ وَعَذَابِ النَّارِ، وَفِتْنَةِ الْقَبْرِ، وَعَذَابِ الْقَبْرِ، وَشَرِّ فِتْنَةِ الْغِنَى، وَشَرِّ فِتْنَةِ الْفَقْرِ، اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنْ شَرِّ فِتْنَةِ الْمَسِيحِ الدَّجَّالِ، اللَّهُمَّ اغْسِلْ قَلْبِي بِمَاءِ الثَّلْجِ وَالْبَرَدِ، وَنَقِّ قَلْبِي مِنَ الْخَطَايَا كَمَا نَقَّيْتَ الثَّوْبَ الْأَبْيَضَ مِنَ الدَّنَسِ، وَبَاعِدْ بَيْنِي وَبَيْنَ خَطَايَايَ كَمَا بَاعَدْتَ بَيْنَ الْمَشْرِقِ وَالْمَغْرِبِ. اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنَ الْكَسَلِ وَالْمَأْثَمِ وَالْمَغْرَمِ

Allohumma inniy a’uuzu bika min fitnati-n-naari va ’azaabi-n-naari va fitnati-l-qobri va ’azaabi-l-qobri va sharri fitnatil-l-g‘inaa va sharri fitnati-l-faqri. Allohumma inniy a’uuzu bika min sharri fitnati-l-masiihi-d-dajjaal. Allohummag‘sil qolbiy bimaa is-salji val-barodi va naqqi qolbiy mina-l-xotoyaa kamaa naqqoyta-s-savba-l-abyado mina-d-danasi va baa’id bayniy va bayna xotoyaaya kamaa ba’dta bayna-l-mashriqi va-l-mag‘rib. Allohumma inniy a’uuzu bika mina-l-kasali va-l-ma’sami va-l-mag‘rom. 

Ma’nosi: “Allohim, Sendan do‘zax fitnasi va do‘zax azobidan, qabr fitnasi va qabr azobidan, boylik fitnasining yomonligidan va faqirlik fitnasi yomonligidan panoh tilayman. Allohim, men Sendan Masih Dajjol fitnasining yomonligidan panoh tilayman. 

Allohim, oq libosni kirlardan pok qilganing kabi qalbimni ham ifloslik, razillikdan pok qilgin va mag‘rib bilan mashriq orasini uzoq qilganingdek, men bilan gunohlar orasini uzoq qilgin.  

Allohim, Sendan dangasalik, gunoh va qarzlardan panoh tilayman”. 
(Buxoriy va Muslim rivoyati) 

•┈•┈•┈•┈•❁✿❁•┈•┈•┈•┈•

اللَّهُمَّ أَنْتَ رَبِّي لّا إِلَهَ إِلَّا أَنْتَ، خَلَقْتَنِي وَأَنَا عَبْدُكَ، وَأَنَا عَلَى عَهْدِكَ وَوَعْدِكَ مَا اسْتَطَعْتُ، وأَعُوذُ بِكَ مِنْ شَرِّ مَا صَنَعْتُ، أَبُوءُ لَكَ بِنِعْمَتِكَ عَلَيَّ، وَأَبُوءُ بِذَنْبِي فَاغْفِرلِي فَإِنَّهُ لَا يَغْفِرُ الذُّنُوبَ إِلَّا أَنْتَ

«Allohumma anta robbiy laa ilaaha illa anta xolaqtaniy va ana ’abduka va ana ’ala ’ahdika va va’dika mastato’tu a’uzu bika min sharri maa sona’tu, abu‘u laka bini’matika ’alayya va abu‘u bizambiy fag‘firliy fainnahu laa yag‘firuz zunuba illa anta»

Ma’nosi: «Allohim! Sen parvardigorimsan, Sendan boshqa iloh yo‘q. Meni Sen yaratding va men Sening qulingman. Men Senga bergan va’damda va Senga bergan ahdimda qodir bo‘lganimcha turibman. Qilgan narsalarimning yomonidan Sening noming bilan panoh tilayman. Menga ato qilgan ne’matlaringga iqror bo‘ldim. Va yana gunohlarimga ham iqror bo‘ldim. Mening gunohlarimni kechir. Chunki Sendan boshqasi gunohlarni kechira olmaydi.
(Buxoriy rivoyati).

•┈•┈•┈•┈•❁✿❁•┈•┈•┈•┈•

اللَّهُمَّ إِنِّي أَسْأَلُكَ الْهُدَى، وَالتُّقَى، وَالْعَفَافَ، وَالْغِنَى

Allohumma inniy as’aluka-l-hudaa va-t-tuqo va-l-’afaafa va-l-g‘inaa. 

Ma’nosi: “Allohim, men Sendan hidoyat, taqvo, salomatlik va boylik so‘rayman”.
(Muslim rivoyati)

Manba: 

@islomuz_quron_bot
</b>"""
    text2="""
<b>
يَا مُقَلِّبَ الْقُلُوبِ ثَبِّتْ قَلْبِي عَلَى دِينِكَ

«Yaa, Muqollibal quluub, sabbit qolbiy ’ala diynika!»

Ma’nosi: «Ey, qalblarni o‘zgartirib turuvchi Zot, qalbimni diningda sobitqadam qilgin!»
(Termiziy rivoyati)

•┈•┈•┈•┈•❁✿❁•┈•┈•┈•┈•

اللَّهُمَّ مُصَرِّفَ القُلُوبِ صَرِّفْ قُلُوبَنَا عَلَى طَاعَتِكَ

«Allohumma musorrifal quluub sorrif quluubana ’alaa to’atik»

Ma’nosi: «Ey qalblarni tasarruf qiluvchi Allohim, qalbimizni toatingga burib qo‘ygin».
(Muslim rivoyati)

•┈•┈•┈•┈•❁✿❁•┈•┈•┈•┈•

اللهُمَّ إِنِّي أَعُوْذُ بِكَ مِنَ الْهَمِّ وَالْحَزَنِ، وَالْعَجْزِ وَالْكَسَلِ، وَالْبُخْلِ وَالْجُبْنِ، وَضَلَعِ الدَّيْنِ وَغَلَبَةِ الرِّجَالِ

«Allohumma inniy a’uuzu bika minal hammi val hazani val ’ajzi val kasali val buxli val jubni va zola’i-d-dayni va g‘olabatirrijaali».

Ma’nosi: «Allohim! Men Sendan tashvishu g‘amdan, ojizlikdan, yalqovlikdan, baxillikdan, qo‘rqoqlikdan, qarzning og‘irligidan va kishilarning (mening ustimdan) g‘olib bo‘lib ketishidan panoh berishingni so‘rayman. 
(Buxoriy rivoyati)

•┈•┈•┈•┈•❁✿❁•┈•┈•┈•┈•

اللَّهمَّ اكفني بِحلالِكَ عن حرامِكَ ، وأغنِني بِفَضلِكَ عَمن سواكَ 

«Allohumma! Ikfiniy bihalaalika ’an haromika va ag‘niniy bifazlika amman sivaaka».

Ma’nosi: «Allohim! Menga haloling ila haromingdan kifoya qilgin. O‘z fazling ila meni o‘zingdan boshqalardan behojat qilgin». 
(Termiziy rivoyati).

•┈•┈•┈•┈•❁✿❁•┈•┈•┈•┈•

لَا إِلَهَ إِلَّا أَنْتَ سُبْحَانَكَ إِنِّي كُنْتُ مِنْ الظَّالِمِينَ

Laa ilaaha illa Anta subhaanaka inniy kuntu minazzolimiyn. 

Ma’nosi: «Sendan o‘zga hech bir iloh yo‘q. Sen barcha aybu nuqsondan pok Zotdirsan. Darhaqiqat, men (o‘z nafsimga) zulm qiluvchilardan bo‘ldim». (Termiziy va Hokim rivoyati).

•┈•┈•┈•┈•❁✿❁•┈•┈•┈•┈•

لَا إِلَهَ إِلَّا اللَّهُ الْعَظِيمُ الْحَلِيمُ، لَا إِلَهَ إِلَّا اللَّهُ رَبُّ الْعَرْشِ الْعَظِيمِ، لَا إِلَهَ إِلَّا اللَّهُ رَبُّ السَّمَوَاتِ، وَرَبُّ الْأَرْضِ، وَرَبُّ الْعَرْشِ الْكَرِيمِ

«Laa ilaaha illallohul ’azimul haliym Laa ilaaha illallohu Robbul ’arshil ’aziym Laa ilaaha illallohu Robbussamavaati va Robbul arzi va Robbul ’arshil Kariym».

Ma’nosi: «Ulug‘ Halim (mehribon) Allohdan O‘zga iloh yo‘q. Arsh egasi Ulug‘ Allohdan o‘zga xech iloh yo‘q. Osmonlar Rabbisi, yer Rabbisi, arsh Rabbisi bo‘lgan Karim Allohdan o‘zga iloh yo‘q». 
(Buxoriy va Muslim rivoyati).

•┈•┈•┈•┈•❁✿❁•┈•┈•┈•┈•

اللَّهمَّ أَصْلِحْ لِي دِينِي الَّذِي هُوَ عِصْمَةُ أَمْرِي، وَأَصْلِحْ لِي دُنْيَايَ الَّتِي فِيهَا مَعَاشِي، وَأَصْلِحْ لِي آخِرَتِي الَّتِي فِيهَا مَعَادِي، وَاجْعَلِ الحَيَاةَ زِيَادَةً لِي فِي كُلِّ خَيْرٍ، وَاجْعَلِ المَوْتَ رَاحَةً لِي مِنْ كُلِّ شَرٍّ

Allohumma aslihliy diini-l-laziy huva ’ismatu amriy va aslih liy dunyaayal-l-latiy fiihaa ma’aashiy va aslih liy aaxiroti-l-latiy fiihaa ma’aadiy vaj’ali-l-hayaata ziyaadatan liy fiy kulli xoyrin vaj’ali-l-rohatan liy min kulli sharrin

Ma’nosi: “Allohim, men uchun ishimning pokligi bo‘lgan dinimni isloh qilgin, hayotim kechadigan dunyoyimni yaxshilagin, qaytar yerim bo‘lgan oxiratimni obod qilgin. Har bir yaxshilikda men uchun hayotimni ziyoda qilgin va men uchun barcha yomonlikdan ko‘ra o‘limni rohat qilgin”.
(Muslim rivoyati) 

•┈•┈•┈•┈•❁✿❁•┈•┈•┈•┈•

اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنْ زَوَالِ نِعْمَتِكَ، وَتَحَوُّلِ عَافِيَتِكَ، وَفُجَاءَةِ نِقْمَتِكَ، وَجَمِيعِ سَخَطِكَ

Allohumma inniy a’uuzu bika min zavaali ni’matika va tahavvuli ’aafiyatika va fujaa’a-ti niqmatika va jamii’i saxotik. 

Ma’nosi: “Allohim, Sendan ne’mating zavolidan, ofiyating ketishidan, daf’atan keluvchi azobingdan va barcha g‘azabingdan panoh so‘rayman”.
(Muslim rivoyati)

@islomuz_quron_bot
</b>"""

    text3="""
<b>
اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنْ شَرِّ مَا عَمِلْتُ، وَمِنْ شَرِّ مَا لَمْ أَعْمَلْ

Allohumma inniy a’uuzu bika min sharri maa ’amiltu, va min sharri maa lam a’mal

Ma’nosi: “Allohim, Sendan qilgan ishlarimning va (hali) qilmagan ishlarimning yomonligidan panoh tilayman”.
(Muslim rivoyati) 

•┈•┈•┈•┈•❁✿❁•┈•┈•┈•┈•

اللَّهُمَّ إِنِّي أَسْأَلُكَ فِعْلَ الْخَيْرَاتِ، وَتَرْكَ الْمُنْكَرَاتِ، وَحُبَّ الْمَسَاكِينِ، وَأَنْ تَغْفِرَ لِي، وَتَرْحَمَنِي، وَإِذَا أَرَدْتَ فِتْنَةَ قَوْمٍ فَتَوَفَّنِي غَيْرَ مَفْتُونٍ، وَأَسْأَلُكَ حُبَّكَ، وَحُبَّ مَنْ يُحِبُّكَ، وَحُبَّ عَمَلٍ يُقَرِّبُنِي إِلَى حُبِّكَ.

Allohumma inniy as’aluka fi’la-l-xoyroti va tarka-l-munkarot va hubba-l-masakiin va an tag‘firo liy va tarhamaniy va izaa arodta fitnata qovmin fatavaffaniy g‘oyro maftuuni va as’aluka hubbak va hubba man yuhibbuk va hubba ’amalin yuqorribuniy ilaa hubbik   

Ma’nosi: “Allohim! Sendan yaxshi amallar qilishni, yomonliklarni tark etishni va kambag‘allarni sevishni hamda mening gunohlarimni kechirishingni va menga rahm qilishingni so‘rayman. Agar qavmning fitnasi (yo‘ldan ozishi)ni istasang, meni bu fitnaga uchmasidan jonimni olgin. Men Sendan O‘zingni sevgingni, Seni sevganlar va Sening muhabbatinga yaqin qiladigan amallar sevgisini so‘rayman”.
(Ibn Moja va Ahmad rivoyati) 

•┈•┈•┈•┈•❁✿❁•┈•┈•┈•┈•

اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنَ الْبَرَصِ وَالْجُنُونِ وَالْجُذَامِ وَمِنْ سَيِّئْ الْأَسْقَامِ 

Allohumma inniy a’uuzu bika mina-l-barosi va-l-junuuni va-l-juzaami va min sayyi’i-l-asqomi

Ma’nosi: “Allohim, Sendan moxovlik, peslik, jinnilik va (barcha) yomon kasalliklardan panoh so‘rayman”
(Abu Dovud, Ahmad va Nasoiy rivoyati) 

•┈•┈•┈•┈•❁✿❁•┈•┈•┈•┈•

اللَّهُمَّ عَافِنِي فِي بَدَنِي ، اللَّهُمَّ عَافِنِي فِي سَمْعِي ، اللَّهُمَّ عَافِنِي فِي بَصَرِي ، لا إِلَهَ إِلا أَنْتَ ،

اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنَ الْكُفْرِ وَالْفَقْرِ ، و أَعُوذُ بِكَ مِنْ عَذَابِ الْقَبْرِ ، لا إِلَهَ إِلا أَنْتَ 

«Allohumma, ’afini fiy badaniy, Allohumma, ’afini fiy sam’iy, Allohumma, ’afini fiy basoriy, laa ilaaha illa Anta! Allohumma, inniy a’uuzu bika minal kufri val faqri va a’uuzu bika min ’azabil qobri laa ilaaha illa Anta».  

Ma’nosi: «Allohim, badanimni, qulog‘imni va ko‘zimni (sog‘lom) ofiyatda qil. Allohim, Sening noming ila kufrdan, kambag‘allikdan va qabr azobidan panoh tilayman. Sendan boshqa iloh yo‘q. 
(Abu Dovud va Ahmad rivoyati). 

•┈•┈•┈•┈•❁✿❁•┈•┈•┈•┈•

 اللَّهُمَّ إنِّي أعُوذُ بِكَ مِنَ العَجْزِ، والكَسَلِ، والجُبْنِ، والبُخْلِ، والهَرَمِ، والقَسْوَةِ، والغَفْلَةِ، والعَيْلَةِ، والذِّلَّةِ، والمَسْكَنَةِ، وأعُوذُ بِكَ مِنَ الفَقْرِ، والكُفْرِ، والفُسُوقِ، والشِّقاقِ، والنِّفاقِ، والسُّمْعَةِ، والرِّياءِ، وأعُوذُ بِكَ مِنَ الصَّمَمِ، والبَكَمِ، والجُنُونِ، والجُذامِ، والبَرَصِ، وَسَيِّىءِ الأَسْقامِ

Allohumma inniy a’uuzu bika mina-l-’ajzi va-l-kasali va-l-jubni va-l-buxli va-l-haromi va-l-qosvati va-l-g‘oflati va-l-’aylati va-z-zillati va-l-maskanati va a’uuzu bika mina-l-faqri va-l-kufri va-l-fusuuqi va-sh-shiqooqi va-n-nifaaqi va-s-sum’ati va-r-riyaa'i va a’uuzu bika mina-s-somami va-l-bakami va-l-junuuni va-l-juzaami va-l-barosi va sayyi'i-l-asqoomi.

Ma’nosi: “Allohim! Men Sendan ojizlikdan, yalqovlikdan, qo‘rqoqlikdan, baxillikdan, qarigandigi ojizlikdan, toshbag‘irlikdan, g‘aflatdan, faqirlikdan, xorlikdan va miskinlikdan panoh so‘rayman va kambag‘allikdan, kufrdan, fosiqlikdan , badbaxtlikdan, munofiqlikdan, sum’a (odamlar eshitsin uchun amal qilish)dan va riyo(xo‘jako‘rsin)dan panoh berishingni so‘rayman, hamda, karlikdan, soqovlikdan, jinnilikdan, pes-mohovlikdan va boshqa yomon kasallikdan ham panoh berishingni so‘rayman”.
(Hokim va Bayhaqiy rivoyati) 

@islomuz_quron_bot
</b>"""
    await mes.answer(text)
    await mes.answer(text2)
    await mes.answer(text3)


@dp.message_handler(text="Duolar kitobi")
async def duolarkitobi(mes: Message):
    await mes.answer_document("https://t.me/Islomiy_Kitoblar_pdf_apk/116", caption="Zikr va duolar dasturi\nAndroid tizimi uchun\n@islomuz_quron_bot")