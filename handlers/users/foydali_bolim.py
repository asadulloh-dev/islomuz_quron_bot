from aiogram.dispatcher.filters import Command

from loader import dp

from aiogram.types import Message
from keyboards.default.foydali_bolim_keyboard import foydali_bolim


@dp.message_handler(text="✅ Foydali bo'lim")
async def foydali(mes: Message):
    await mes.answer("Foydali bo'lim:", reply_markup=foydali_bolim)


@dp.message_handler(text="Allohning 99 ismlari")
async def asmaul(mes: Message):
    text = """
Allohning borligiga ishongan odam U zotni yaxshi tanishi ham kerak. Aqoid ilmi istilohi bilan aytganda ma’rifat hosil qilishi lozim. Bu ma’rifat esa Alloh taoloning go‘zal ismlari va U zotning sifatlarini bilish ila hosil bo‘ladi.

    Alloh taolo: <b>«Allohning go‘zal ismlari bordir. Bas, Unga o‘sha (ism)lar ila duo qiling»</b>, degan (A’rof: 180-oyat).
Allohning barcha ismlari go‘zaldir. Mo‘min-musulmon banda Allohga duo qilganida, o‘sha go‘zal ismlar ila duo qilmog‘i lozim.

Alloh taolo “Isro” surasida:  <b>«Allohga duo qilinglar, Rahmonga duo qilinglar, qaysisiga duo qilsangiz ham, bari bir. Go‘zal ismlar Unikidir»</b>, degan (110-oyat).

Abu Hurayra roziyallohu anhudan rivoyat qilinadi: «Nabiy sollallohu alayhi va sallam: <b>«Allohning to‘qson to‘qqizta ismi bor. Kim ularni yod olsa, jannatga kiradi. Albatta, Alloh toqdir va toqni yaxshi ko‘radi»</b>, dedilar». Ikki shayx va Termiziy rivoyat qilgan.
Alloh toq bo‘lgani va toqni yaxshi ko‘rgani uchun ham Uning go‘zal ismlari to‘qson to‘qqizta bo‘lgan. Kim o‘sha to‘qson to‘qqiz ismni yod olsa jannatga kiradi. Chunki bu go‘zal ismlarni yod olgan kishi Alloh taoloning go‘zal ismlarini doimo zikr qilib yuradigan banda bo‘ladi.
Ammo bu Alloh taoloning to‘qson to‘qqizdan boshqa ismi yo‘q degani emas. Albatta, Alloh taoloning ismlari ko‘p.
Qo‘yidagi hadisi sharifda Alloh taoloning go‘zal ismlari sifatida mashhur bo‘lgan to‘qson to‘qqiz ismni zikri keladi.

Yana o‘sha kishidan rivoyat qilinadi: <b>«Allohning to‘qson to‘qqizta ismi bor. Kim ularni to‘liq bilib olsa, jannatga kiradi. U Undan o‘zga ilohu ma’bud yo‘q Allohdir. Rahmon, Rohiym, Malik, Quddus, Salom, Mo‘min, Muhaymin, Aziz, Jabbor, Mutakabbir, Xoliq, Bari’, Musavvir, G‘affor, Qahhor, Vahhob, Razzoq, Fattoh, Aliym, Qobiz, Bosit, Xofiz, Rofe’, Mu’izz, Muzill, Samiy’, Basiyr, Hakam, Adl, Latiyf, Xabiyr, Haliym, Aziym, G‘afur, Shakur, Aliy, Kabiyr, Hafiyz, Muqiyt, Hasiyb, Jaliyl, Kariym, Raqiyb, Mujiyb, Vose’, Hakiym, Vadud, Majiyd, Bo’is, Shahiyd, Haq, Vakiyl, Qaviy, Matiyn, Valiy, Hamiyd, Muhsiy, Mubdi’, Mu’iyd, Muh’yi, Mumiyt, Hayy, Qayyum, Vojid, Vohid, Somad, Qodir, Muqtadir, Muqaddim, Muaxxir, Avval, Oxir, Zohir, Botin, Voliy, Mutaoliy, Barr, Tavvob, Muntaqim, Afvvu, Ra’uf, Molikul Mulk, Zul Jalol val Ikrom, Muqsit, Jome’, G‘aniy, Mug‘niy, Mone’, Zorr, Nofe’, Nur, Hodiy, Badiy’, Boqiy, Voris, Rashiyd va Sabur»</b>, dedilar». Termiziy, Ibn Hibbon va al-Hokim rivoyat qilgan.


Batafsil: https://telegra.ph/Asmaul-husna-04-06
Manba: https://islom.uz/maqola/149

@islomuz_quron_bot"""
    await mes.answer(text)
    await mes.answer_document("https://t.me/islomiy_mediya/12", caption="""
Asmaul Husna dasturi

Android tizimi uchun
<a href="https://apps.apple.com/us/app/асмаул-ҳусна/id1482753809">IOS tizimi uchun link</a>

Alloh taoloning go'zal ismlarini, ma'nolarini jamlagan dastur

Nashriyot: @HilolNashr

@islomiy_mediya
@islomuz_quron_bot""")
    await mes.answer_video("https://t.me/islomiy_mediya/645", caption="@islomuz_quron_bot")
    await mes.answer_video("https://t.me/islomiy_mediya/646", caption="@islomuz_quron_bot")


@dp.message_handler(text="40 farz")
async def qirqfarz(mes: Message):
    text = """
Shariatimizda farzlar ko‘p, lekin ota bobolarimiz quyidagi qirq farzni alohida muhim sanab, yosh avlodga yod oldirishgan. Musulmon kishi qirq farzni yaxshi bilib olishi va ularga muntazam amal qilishi lozim.

Farz nima ? Shariat qat’iy dalil bilan talab qilgan ish farz deyiladi. Farz amalni qilish har bir mo‘min musulmonga lozimdir. Uni bajargan kishi savob oladi, bajarmagan osiy bo‘lib, iqob – jazoga qoladi, inkor etgan odam esa kofir bo‘ladi.

QIRQ FARZ

Islomda beshta farz bor:
1. Iymon;
2. Namoz;
3. Ro‘za;
4. Zakot;
5. Haj.

Iymonda yettita farz bor:
1. Allohga ishonish;
2. Allohning farishtalariga ishonish;
3. Allohning kitoblariga ishonish;
4. Allohning payg‘ambarlariga ishonish;
5. Oxirat kuniga ishonish;
6. Qadarga – yaxshilik ham, yomonlik ham Alloh taoloning irodasi bilan bo‘lishiga ishonish;
7. O‘lgandan keyin qayta tirilishga ishonish.

Tahoratning farzlari to‘rtta:
1. Yuzni to‘la yuvish;
2. Qo‘llarni tirsaklar bilan qo‘shib yuvish;
3. Boshning to‘rtdan biriga mash tortish;
4. Oyoqlarni to‘pig‘i bilan qo‘shib yuvish.

G‘uslning farzlari uchta:
1. Og‘izni g‘arg‘ara qilib chayish;
2. Burunni achishtirib chayish;
3. Badanning hamma joyiga suv yetkazib yuvish.

Tayammumning farzlari to‘rtta:
1. Niyat;
2. Pok tuproqni qasd qilish;
3. Ikki qo‘lni toza tuproqqa urib, yuzga surish.
4. Ikki qo‘lni tuproqqa urib, tirsak bilan surish

Namozning farzlari o‘n ikkita bo‘lib, oltitasi
namoz tashqarisidadir, ular «namozning shartlari», deyiladi:
1. Badanning (junub, tahoratsizlik, hayz, nifosdan) pok bo‘lmog‘i;
2. Kiyimning pok bo‘lmog‘i va avratning to‘silmog‘i;
3. Namoz o‘rnining pok bo‘lmog‘i;
4. Namoz vaqtining kirmog‘i;
5. Qiblaga yuzlanib o‘qimoq;
6. Dildan (xolis) niyat qilmoq;

Oltitasi namoz ichida bo‘lib, ular «namozning ruknlari deyiladi:
1. Namozga takbiri tahrima bilan kirish;
2. Qiyom;
3. Qiroat;
4. Ruku’;
5. Sajda;
6. Qa’dai oxir.

Yana quyidagilar ham farzdir:
1. Ilm olish;
2. Amri ma’ruf va nahyi munkar;
3. Hayz va nifos ilmini bilish;
4. Rizqni halol yo‘l bilan topish;
5. Shariat halol deb belgilagan narsalarnigina yeyish.
Manba: vakillik.uz

@islomuz_quron_bot
"""
    await mes.answer(text)


@dp.message_handler(text="Islomning 5 ustuni")
async def beshustun(mes: Message):
    text = """
Payg‘ambarimiz alayhisalom marhamat qilib aytdilarki: “Islom beshta ustun ustiga qurildi. Birinchisi “La ilaha ilalloh, Muhammadun rasulalloh”, deb shahodat berishlik. Ikkinchisi namoz o‘qish. Undan keyingisi zakot berishlik va undan keyingisi haj qilishlik va oxirgisi ro‘za tutishlikdir”. 

Besh ustundan biri shahodat. Bilamizki, Islom dini oldingi dinlarni to‘ldiruvchisi, ularning davomchisidir. Payg‘ambarimizga yangi din yuborilgani yo‘q. U Zot o‘zlaridan oldin kelgan payg‘ambarlarning dinini davom ettirdilar. Hamma payg‘ambarlarning so‘zi bitta edi – Allohdan boshqa iloh yo‘q. Insonni musulmon qiladigan, uni boshqa din vakillaridan ajratadigan, iymonining belgisi shahodatdir. Musulmon kishining asosiy belgisi bu – Allohga iymon keltirish va Allohni bizga tanitgan zot Muhammad (s.a.v)ni payg‘ambar, rasul ekanliklarini e'tirof etish.

Ikkinchi ustun – namoz. Payg‘ambarimiz (s.a.v) aytadilarki: “G‘ayridin va musulmonning o‘rtasidagi farq namozdir”. Namoz shunday bir ibodat-ki, uni tark etishga biron-bir insonga yo‘l yo‘q. Ba'zi bir insonlar o‘z holatlaridan norozi bo‘lishar, lekin ayni haqiqat shu-ki, musulmonman deb da'vo qilib turib, masjidning eshigini topolmaydigan, umrida biror marta peshonasi sajda ko‘rmagan, namoz o‘qishlikni bilmaydigan inson, Alloh saqlasin, nasroniylarning fe'lini qilib turgan odamga o‘xshaydi. Chunki nasroniylar biz nasroniymiz deydi, lekin ibodatlarini qilishmaydi.

Navbatdagi uchinchi ustun – zakot berish. Zakot moliyaviy ibodat bo‘lib, ya'ni insonning moli ma'lum bir darajaga yetganidan so‘ng o‘shandan ma'lum bir qismini ehson qiladi. Ammo bu hammaga ham emas. Bu imkoniyati bor, moli o‘sha darajaga yetgan mo‘min-musulmonlar uchun. Masalan, qo‘yi 40taga yetgan inson, ulardan birini zakot qiladi. Shu hisobga yetmaguncha zakot bermaydi. 

Undan keyingi farz – haj qilishlikdir. Bu farz ham moddiyatga taalluqli bo‘lgan ibodatdir. Moddiy tomondan hajga borib kelishga qurbi yetadigan, salomatligi ko‘taradigan kishiga umrida bir marta haj qilishlik farz hisoblanadi.

So‘nggi beshinchi farz – Ramazon oyida ro‘za tutmoqlikdir. Bu ibodatni namoz ibodati bilan solishtiradigan bo‘lsak, ro‘zaning farqi badaniy, jismiy ibodat hisoblanadi. Shuning uchun bunda sog‘lik shart. Agar bir insonda ro‘zadan to‘sadigan kasallik bo‘ladigan bo‘lsa, undan to tuzalgunga qadar ro‘za tutish soqit bo‘ladi. Agar surunkali bo‘lsa, u inson ro‘zasining evaziga fidyasini beradi

@islomuz_quron_bot
"""
    await mes.answer(text)


@dp.message_handler(text="Amallarning hukmlari")
async def amallaningturlari(mes: Message):
    text = """
"Fiqh" so‘zining lug‘aviy ma’nosi "idrok etmoq", "anglamoq", "tushunib yetmoq"dir. Istilohda esa bu so‘z, ochiq dalillar bilan buyurilgan amallar, ya’ni bevosita etiqodga tegishli bo‘lmagan namoz, ro‘za, zakot kabi masalalarga oid shariy hukmlarni o‘rganish ilmini anglatadi.

Foydalari:

— Alloh taoloning rizoligiga mos amallarni to‘g‘ri ado etishni o‘rgatadi;
— dunyoda baxtli, saodatli bo‘lish, jaholat jarligidan bilim cho‘qqisiga yuksalish yo‘lini ko‘rsatadi;
insonlarga foydali va zararli bo‘lgan narsalarni bayon qilish imkoniyatini beradi; oxiratda esa, do‘zaxdan saqlanib, jannatdagi abadiy ne’matlarga yetishuvimizga sabab bo‘ladi.

Shariy hukmlarning qismlari

Shariy hukmlar quyidagi qismlarga ajratilgan:

1. Farz 
Farz qat'iy, ochiq shariy dalil bilan bajarilishi amr etilgan amaldir. Besh vaqt namoz, ro‘za, zakot kabi.

Farzning hukmi
Farzni inkor qilgan kishi kofir bo‘ladi. Ishonib, amal qilmagan kishi fosiq bo‘lib, Alloh taolo tomonidan belgilangan jazoga loyiq bo‘ladi.
Farz ham ikki qismdir: farzi ayn va farzi kifoya.
a) Farzi ayn mukallaf har bir kishi bajarishi shart bo‘lgan farzdir. Besh vaqt namoz, ro‘za, zakot kabi.
Mukallaf har bir kishi bu amallarni shaxsan o‘zi bajarishi zarur. Bir qism odamlarning farzi aynni bajarishi boshqalar zimmasidan bu masuliyatni soqit qilmaydi.
b) Farzi kifoya ba’zi musulmonlar bajarishi bilan boshqalar zimmasidan tushadigan farzdir. Masalan, janoza namozini o‘qish kabi.
Farzi kifoyani hech kim ado etmasa, barcha gunohkor bo‘ladi.

2. Vojib 
Ochiq bo‘lmagan shariy dalillar bilan bajarilishi takidlangan amal (Ramazon va Qurbon hayiti namozlari, namozda (zam suradan avval) Fotiha surasini o‘qish kabi).
Hukmi. Bajarilishi lozim (vojib) bo‘lib, uni inkor etgan kishi kofir bo‘lmaydi. Vojibni bajargan kishi savob oladi. Tark qilgan kishi esa, jazoga loyiq bo‘ladi.

3. Sunnat 
Sunnat ikki qismga bo‘linadi:
a) Sunnati muakkada: Payg‘ambarimizning, sollallohu alayhi va sallam, har doim bajarib, juda kam holatlarda tark qilgan sunnatlaridir Tahoratda og‘zini suv bilan chayish kabi.
b) Sunnati g‘ayri muakkada: Payg‘ambarimizning, sollallohu alayhi va sallam, ba’zan bajarib, ba’zan tark qilgan sunnatlaridir.
Hukmi. Sunnat amalni bajargan kishi savobga erishadi. Uni tark qilish karih va zararlidir.

4. Harom 
Qattiy, ochiq shariy dalillar bilan bajarilishi taqiqlangan amal. Zino, o‘g‘rilik qilmoq kabi.
Hukmi. Harom ishni qilgan kishi do‘zax azobiga giriftor bo‘ladi. Tark qilgan kishi esa, Allohning amriga itoat qilgani uchun savobga erishadi, haromni inkor qilgan odam kofir bo‘ladi.

5. Karohati tahrimiya 
Ochiq bo‘lmagan dalillar bilan bajarilishi taqiqlangan amal. Boshqa kishining savdo-sotig‘iga daxl qilib, u olmoqchi bo‘lgan molni olish yoki boshqa kishi sovchi qo‘ygan qiz yoki ayolning qo‘lini, u voz kechmasdan oldin so‘rash kabi.
Hukmi. Buni qilgan odam harom ishni bajargan kabi azobga duchor bo‘ladi. Lekin inkor qilgan kishi kofir bo‘lmaydi.

6. Karohati tanzihiya
Ochiq bo‘lmagan shariy dalillar bilan bajarilishi taqiqlangan amallar.
Hukmi. Bu amalni bajargan kishiga hech qanday jazo va dashnom berilmaydi. Lekin yaxshi va fazilatli amallarning aksini qilgan bo‘ladi.

7. Muboh 
Qilish yoki qilmaslikda insonlar erkin bo‘lgan amal.
Hukmi. Bajarilgan paytda savob ham, tark etilgan paytda jazo ham berilmaydi.
Manba: https://islom.ziyouz.com/fiqh

@islomuz_quron_bot"""
    await mes.answer(text)


@dp.message_handler(text="Salovat")
async def salovat(mes: Message):
    text = """
Rasululloh sollallohu alayhi vasallamga salavot aytishga Alloh subhanahu va taolo amr qilgan. Bu haqda Ahzob surasining 56-oyatida quyidagicha marhamat qilingan:  

 إِنَّ اللَّهَ وَمَلائِكَتَهُ يُصَلُّونَ عَلَى النَّبِيِّ يَا أَيُّهَا الَّذِينَ آمَنُوا صَلُّوا عَلَيْهِ وَسَلِّمُوا تَسْلِيمًا

 «Albatta, Alloh va Uning farishtalari Payg‘ambarga salavot ayturlar. Ey iymon keltirganlar! Siz ham unga salavot ayting va salom yuboring».

Allohning amri bandalar uchun farz-vojib hisoblanadi. Shuning uchun ham ulamolarimiz har bir kishi umri davomida bir marta Rasululloh sollallohu alayhi vasallamga salavot aytishi farzdir, deydilar.

Shofe’iy mazhabida namozning so‘ngida (tashahhudda) salavot aytmoqlik vojib amal hisoblanadi. Imom Shofe’iy rahmatullohi alayhi: «Tashahhudda Rasululloh sollallohu alayhi vasallamga salavot aytilmasa, namoz namoz bo‘lmaydi» deganlar. Hanafiy mazhabida esa, bu amal sunnat hisoblanadi.

Namozdan tashqarida barcha vaqtlarda salavot aytish mustahabdir. Lekin Payg‘ambarimiz sollallohu alayhi vasallamning ismlari, kunyalari 1 (Abul Qosim) yoki Rasululloh, Payg‘ambarimiz, Nabiy kabi lafzlar bilan u zot alayhissalom zikr qilinsalar, salavot aytish lozim bo‘ladi. Bir majlisda ismlari bir necha marta tilga olinsa, boshida bir marta salovot aytmoqlik vojibdir, qolganlari esa sunnat. Ba’zi ulamolar har safar salavot aytmoq vojib deganlar. Salavot aytish «Solallohu alayhi vasallam», «alayhissalom» yoki boshqa lafzlar bilan bo‘ladi.

«Sollallohu  alayhi  vasallam»   degani «Unga Allohning salavoti va salomi bo‘lsin!» deganidir.
    
Solatul tunajjiyna
Allohumma solli ʼala sayyidinaa Muhammadin solaatan tunjiynaa bihaa min jamiyʼil ahvaali val aafaati va taqziy lanaa bihaa jamiyʼal haajaati va tutahhirunaa bihaa min jamiyʼis sayyi`aati va tarfaʼunaa bihaa ʼindaka aʼlaad darajaati va tuballigʻunaa bihaa aqsol gʻooyoti min jamiyʼil xoyroti fil hayati va baʼdal mamaati va ʼala olihi va sohbihi va sallim tasliiman kasiyron!

Maʼnosi: "Allohim! Sayyidimiz Muhammad sollallohu alayhi vasallamga salavot va salomlar boʻlsin. (Allohning fazli va marhamati bilan), oʻsha salavot sababli barcha qiyinchilik va balo ofatlardan najot ber. Salavot sababli barcha hojatlarimizni baroridan keltir. Salavot sababli barcha yomonliklardan bizni pokla. Salavot sababli Huzuringdagi darajalarga bizlarni yuksaltir. Salavot sababli hayot va oʻlimdan keyingi barcha yaxshiliklarni eng yuqori darajasiga bizlarni koʻtar. Rasulullohning oilalariga va sahobalariga koʻplab salavot va salomlar boʻlsin!".

Izoh: Ulamolar tajribalariga muvofiq ushbu tunajjiynaa salavotini 1111 marta yaxshi bir narsani niyat qilib oʻqilsa, Alloh izni bilan maqsad hosil boʻlishi umid qilinadi.

Tunajjiyna - najot beruvchi, deganidir. Bu salavotni bunday nomlanishiga sabab, chunki u gʻam va muammolardan najot berib, bartaraf qilgani uchundir.

Solatan nariya
اللَّهُمَّ صَلِّ صَلاَةً كَامِلَةً وَسَلِّمْ سَلاَماً تَامًّا عَلَى سَيِّدِنَا مُحَمَّدٍ تَنْحَلُّ بِهِ الْعُقَدُ وَتَنْفَرِجُ بِهِ الْكُرَبُ وَتُقْضَى بِهِ الْحَوَائِجُ وَتُنَالُ بِهِ الرَّغَائِبُ وَحُسْنُ الْخَوَاتِمِ وَيُسْتَسْقَى الْغَمَامُ بِوَجْهِهِ الْكَرِيمِ وَعَلى آلِهِ وَصَحْبِهِ فِي كُلِّ لَمْحَةٍ وَنَفَسٍ بِعَدَدِ كُلِّ مَعْلُومٍ لَكَ  


«Allohumma, solli solaatan kaamilatan va sallim salaaman taamma ’alaa sayyidinaa Muhammadin allaziy tanhallu bihil ’uqod, va tanfariju bihil kurob, va tuqzoo bihil havaaij, va tunaalu bihir-rog‘ooib, va husnul xovaatiymi va yustasqol-g‘omaam, bi vajhihil kariym va ’alaa aalihi va sohbihi va sallim». 

«Allohim! Sayyidimiz Muhammad sollallohu alayhi vasallamga mukammal, to‘liq salavot va salomlar bo‘lsin. Allohning fazli va marhamati bilan, o‘sha salavot sababli jumboqlar yechilur, mashaqqatlar barham topur, hojatlar baroridan kelur, rag‘bat qilingan narsalar qo‘lga kiritilur, yaxshi xotimaga erishilur hamda bulutlardan yomg‘ir yog‘ur. U zotning oilalariga va sahobalariga ham salavotu salomlar bo‘lsin».
Naariya – yondiruvchi olov deganidir. Salavotning bunday nomlanishiga sabab shuki, u g‘am va muammolarni tezlik bilan kuydirib tashlaydi.

@islomuz_quron_bot"""
    await mes.answer(text)


@dp.message_handler(text="Manbalar va foydali saytlar")
async def manbalarvakanallar(mes: Message):
    text = """
<b>
islom.uz(islam.uz) Shayx Muhammad Sodiq Muhammad Yusuf rahimahulloh tomonidan asos solingan sayt
muslim.uz O'zbekiston Musulmonlari idorasining rasmiy sayti
vakillik.uz O'MI Toshkent shaxar vakilligi
muslimaat.uz Muslimalar uchun
quran.uz Qur'onga oshiq qalblar uchun
savollar.islom.uz Zikr ahlidan so'rang
arabic.uz Arab tilini o'rganamiz
fiqh.uz Fiqh akademiyasi
hadis.islom.uz Hadislar
siyrat.uz Rosululloh alayhisalom va sahobalarning hayoti
madrasa.uz Yurtimizdagi madrasalar
masjid.uz Yurtimiz masjidlari
tazkiya.uz Ruhiy tarbiya
mehrob.uz Shayx Rahmatulloh Termiziy saytlari


@islomuz_quron_bot
</b>"""
    await mes.answer(text)
