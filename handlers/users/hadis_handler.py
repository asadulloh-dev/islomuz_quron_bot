from loader import dp

from aiogram.types import Message
from keyboards.default.hadis_keyboard import hadis, muhaddislar, hadis4


@dp.message_handler(text="Hadis")
async def hadislarb(mes: Message):
    await mes.answer("Hadis bo'limi: ", reply_markup=hadis)


# 1 Hadis nima?

@dp.message_handler(text="Hadis nima?")
async def hadisna(mes: Message):
    hadisnima = """
<b>Ushbu risolada hadis haqida qisqa ma'lumot berilgan:
Hadis (arabchadan — xabar, gap, yangilik) — Payg'ambarimiz Muhammad sollallohu alayhi va sallamning aytgan so'zlari, qilgan ishlari toʻgʻrisidagi rivoyat. Hadislar Islom dinida Qurʻon karimdandan keyin ikkinchi manba hisoblanadi.
Qurʼonda barcha huquqiy va axloqiy masalalar umumiy tarzda bayon etilgan. Ularga aniqlik kiritish va izohlash uchun Rosululloh alayhisalom hadislarni aytganlar.

Hadis 2 qismdan iborat boʻladi: matn va isnod(Matnga olib boruvchi kishilar  silsilasi).

Hadislar eʼtiborga olinishi jihatidan 3 qismga boʻlinadi:
1) sahih (ishonchli)   2) hasan (yaxshi)   3) zaif.

Rosululloh alayhisalomning vafotlaridan keyin hadislarni naql qilish odat tusiga kirdi.Shu munosabat bilan bir guruh musulmonlar uni yozma shaklda to'play boshladilar, lekin bu to'plamlar muayyan tartibga solinmagan, boblarga ajratilmagan edi.
Keyinchalik ba'zi ixtiloflar, ziddiyatlar, yolg'onchilik oqibatida ko'plab ishonarsiz, to'qima hadislar yuzga kelgan.
Davr o'tishi bilan 9-10 asrlarda hadislarning eng ishonchli 6 ta to'plami vujudga keldi:
"Sahihi Buxoriy"
"Sahihi Muslim"
"Sunani Termiziy"
"Sunani Abu Dovud"
"Sunani Ibn Moja"
"Sunani Nasoiy"

Hadis 2 turga — Hadisi qudsiy va Hadisi nabaviyga boʻlinadi:
Aytilishi(lafzi) Rasululloh alayhissalom tomonidan, ma'nosi Alloh tarafidan boʻlgan hadislarlar "Hadisi Qudsiy" deyiladi. Bunday hadislar ikki yuz atrofidadir deyiladi.
Payg'ambar alayhissalomning hadislariga kelsak, ular u zotning so'zlari (qavllari), harakatlari, ahkomlari, shakli-shamoyillari hamda xulqiy fazilatlari va sifatlarini qamrab, bunda lafz ham, ma'no ham Rasulullohning o'zlaridan sodir bo'lgandir.

Muhaddis - hadis ilmi ila ularni rivoyat qilish va chuqur oʻrganish jihatidan shugʻullanuvchi kishi.

@islomuz_quron_bot</b>
"""
    await mes.answer(hadisnima)


# 2 Hadis ilmi lug'ati

@dp.message_handler(text="Hadis ilmi lug'ati")
async def lugat(mes: Message):
    text1 = """<b>
Hadis ilmiga doir istilohiy lugʻatlar

Mustalahul hadis ilmi – bir necha usul va qoidalarni oʻrgatadigan ilmdir.
Hadis – Nabiy sollallohu alayhi vasallamdan asar boʻlib qolgan gap, ish, taqrir, xalqiy (tana tuzilishi), xulqiy sifatlar va tarjimai holga tegishli maʼlumotlar.
Xabar – hadisning murodifi (sinonimi). Xabar ham, hadis ham bir xil maʼnodagi narsa, yaʼni, ularning orasida farq yoʻq.
Asar – hadisga teskari boʻlib, u hadis bilan bir xil maʼnoni ifoda etmaydi. «Asar» deganda, sahoba va tobeʼinlarga nisbat berilgan soʻzlar va feʼllar tushuniladi.
Isnod – bir soʻzni uning aytuvchisiga nisbat berish, suyab qoʻyish, bu gapning egasi falonchi, deyish.
Sanad – matnga olib boruvchi kishilarning silsilasi.
Matn – kalomning sanadi yetib borgan narsa.
Musnad –«sanad» maʼnosida ham ishlatiladi. Bunda musnad «masdari miymiy» («mim»li masdar) maʼnosini ifoda qilgan boʻladi.
Musnid – hadisni sanadi bilan rivoyat qiluvchi shaxsdir. U oʻzi rivoyat qilgan hadisni ilm tarzida biladimi yoki yodlab olib gapiryaptimi, farqi yoʻq.
Muhaddis– hadis ilmining rivoyati va diroyati bilan mashgʻul boʻlgan kishidir.
Hofiz – bu narsada yana ham keng koʻlamga erishib, shayxlari va shayxlarining shayxlarini tabaqama–tabaqa yaxshi biladigan va har bir tabaqada bilgani bilmaganidan koʻp boʻlgan kishi.
Hokim – hadisga bogʻliq hamma ilmni ihota qilib olgan odam. Uning bilmagan narsasi juda oz boʻladi.
Amirul moʻʼminiyn– hadis ilmida eng peshqadam olimlardan boʻlib, oʻz asrlarining koʻzga koʻringan shaxslari sanalganlar.
Mutavotir xabar – muayyan adad bilan chegaralanmagan yoʻllar bilan bizga yetib kelgan xabar.
Ohod xabar – bizga yetib kelguncha boʻlgan yoʻllari muayyan adad bilan chegaralangan xabar.
Mashhur – har bir tabaqada uch va undan ortiq odam rivoyat qilgan, ammo tavotur darajasiga yetmagan hadis.
Mustafiyz – Mustafiyz mashhurdan koʻra xosroqdir. Chunki mustafiyzda sanadning ikki tarafida (boshidan oxirigacha) roviylar soni bir xil boʻlishi shart qilib qoʻyilgan.
Aziz – roviylari barcha tabaqalarida ikkitadan kam boʻlmagan hadis.
Gʻariyb – bitta roviy yolgʻiz oʻzi rivoyat qilgan hadis.
Siqa – ishonchli roviy.
Maqbul xabar – xabar beruvchisining sodiqligi ustun kelgan xabar.
Mardud – rad qilingan, qabul qilinmagan xabar. U xabar beruvchisining sodiqligi ustun boʻlmagan, yaʼni uning rostgoʻy emasligi aniqlangan xabar.
Sahih hadis – sanadi boshidan oxirigacha adolatli va zobtli kishi oʻziga oʻxshagan adolatli va zobtli kishidan muttasil (uzluksiz) sanad ila naql qilgan hamda shozz va illatli boʻlmagan hadis.
Muttafaqun alayhi – imom Buxoriy va imom Muslimning biror bir matnga ittifoq qilganidir.
Hasan hadis – sanadi muttasil boʻlib, zobti yengilroq odil kishi oʻz mislidan oxirigacha rivoyat qilgan hamda shuzuz va illati boʻlmagan hadis.
Muhkam – maqbul hadis boʻlib, oʻziga oʻxshagan boshqa bir hadisga teskari boʻlishdan salomat.
Muxtaliful hadis – maqbul hadis boʻlib, oʻziga oʻxshagan hadisga zohiran qarshi maʼnoda keladi. Ularning ikkisining maʼnosini qoʻshib, jamlash mumkin.
Nasx – shariat sohibining avval sodir boʻlgan hukmni undan keyin kelgan hukm bilan koʻtarishi.
Mardud – xabar beruvchining sodiqligi ustun boʻlmagan xabardir.
Zaif hadis – hasan sifatini uning shartlaridan birining yoʻqolishi tufayli oʻzida toʻliq jamlamagan narsa.
Muallaq hadis – sanadining avvalida bitta yoki undan koʻp roviy ketma–ket tushirib qoldirilgan hadis.
Mursal hadis – sanadining oxiridan tobeʼindan keyin birorta roviy tushib qolgan hadis.
Moʻʼzal hadis – sanadidan ikki va undan ortiq roviy ketma–ket tushib qolgan hadis.
Munqoteʼ hadis – sanadi muttasil boʻlmagan, yaʼni ulanib kelmagan, kesilishi bor hadis.
Mudallas – sanaddagi aybi maxfiy tutilgan va sirtdan koʻrinishini yaxshilashga urinilgan hadis.
Maxfiy mursal – roviyning oʻzi muloqotda boʻlgan yoki bir asrda yashagan odamdan bevosita oʻzi eshitmagan narsani rivoyat qilishi.

@islomuz_quron_bot</b>
"""
    text2 = """
<b>
Muʼanʼan xabar – roviy rivoyatni «an fulan an fulan» deb keltirishi.
Muannan – roviy «Falonchi bizga «albatta (anna – أنَّ) falonchi…» deb hadis aytdi» deb rivoyat qilgan hadis.
Mavzuʼ xabar – toʻqilgan yolgʻon boʻlib, sunʼiy ravishda keltirilgan va Rasululloh sollallohu alayhi vasallamga nisbat berilgan xabar.
Matruk hadis – sanadida yolgʻonchilikda ayblangan roviysi bor hadis.
Munkar – sanadida katta xatosi boʻlgan yoki gʻaflati koʻpaygan yohud fisqi zohir boʻlgan roviy bor hadis.
Maʼruf hadis – zaif roviy qilgan rivoyatga muxolif tarzda ishonchli roviyning qilgan rivoyati.
Shozz hadis – hadisi maqbul boʻlgan odam oʻzidan koʻra yaxshiroq roviyga muxolif ravishda rivoyat qilgan hadis.
Mahfuz – siqaligi oʻta kuchli odam oddiy siqa odamga xilof ravishda hadis rivoyat qilishi.
Muʼallal – sirtdan qaralganda illati bilinmaydigan, lekin sahihligiga futur yetkazadigan illati topilgan hadis.
Mudraj – isnodining siyoqi oʻzgartirilgan yoki matniga oʻzidan boʻlmagan narsa (undan emasligi koʻrsatilmasdan) kiritilgan hadis.
Maqlub – hadis sanadida yoki matnida bir lafzning oʻrniga boshqasini keltirish, avval yoki oxiriga surib qoʻyish va shunga oʻxshash ishlar.
Muztorib hadis – turli yoʻllar ila bayon qilingan va quvvati teng boʻlgan rivoyat.
Musahhaf – hadisdagi siqa roviylar rivoyat qilgan bir soʻzning lafzini yoki maʼnosini almashtirib qoʻyish.
Bidʼat – din tugal boʻlganidan soʻng unga bir yangilik kiritish. Yoki Nabiy sollallohu alayhi vasallamdan keyin havoyi nafsga berilib, shariatda boʻlmagan baʼzi bir amallarni yangidan paydo qilish.
Hadisi qudsiy – Nabiy sollallohu alayhi vasallamdan naql qilingan va Alloh taologa isnod berilgan hadis.
Marfuʼ hadis – Nabiy sollallohu alayhi vasallamga izofa qilingan soʻz, feʼl, taqrir yoki sifatdan iborat.
Mavquf hadis – sahobiyga izofa berilgan soʻz yoki feʼl yoki taqrir.
Maqtuʼ– tobeʼinga yoki undan past darajadagi roviyga izofa qilingan gap yoki amal.
Musnad – sanadi Nabiy sollallohu alayhi vasallamga koʻtarib yetkazilgan xabar.
Muttasil xabar – marfuʼ boʻladimi, mavquf boʻladimi, kimga yetkazilishidan qatʼiy nazar, sanadi ulangan, kesilmagan xabar.
Eʼtibor – bitta roviy rivoyat qilgan hadisni boshqalar ham rivoyat qilgan yoki qilmaganligini bilish uchun shu hadisning yoʻllarini izlash.

@islomuz_quron_bot</b>
"""

    text3 = """
<b>
Mutobeʼ – roviyning yakka oʻzi rivoyat qilgan hadisining lafziga va maʼnosiga yoki faqat maʼnosiga muvofiq tarzda kelgan boshqa bir hadisdir. Faqat ikkala taraf rivoyat qilayotgan sahobiy bir kishi boʻlishi kerak.
Shohid– yolgʻiz roviy rivoyat qilgan hadisning lafziga va maʼnosiga yoki faqat maʼnosiga muvofiq tarzda kelgan hadisdir. Faqat mazkur ikki hadisni rivoyat qilayotgan sahobiylar boshqa–boshqa boʻlishi kerak.
Tahammul – shayxlardan hadisni qabul qilib olish yoʻllari.
Ijozat – shayx shogirdining hadislarni ogʻzaki yoki yozma ravishda rivoyat qilishiga ruxsat bermogʻi.
Munovala – shayx kitobini tolibi ilmga tutqazib: «Bu mening falonchidan qilgan rivoyatim, uni mendan rivoyat qil», deydi. Shayx uni tolibi ilmga mulk qilib yoki vaqtinchalikka, koʻchirib olishi uchun beradi.
Eʼlom – shayxning tolibga «Bu hadis yoki bu kitob eshitgan rivoyatlarimdan» deb bildirib qoʻyishi – maʼlumot berishi.
Vasiyat – shayx oʻlimidan yoki safaridan oldin biror kimsaga oʻzi rivoyat qilib yurgan kitoblaridan birini vasiyat qilishi.
Vijoda – tolib oʻzi eshitmagan, ijozati ham boʻlmagan bir shayxning qoʻlyozmasini topib oladi va uning dastxatini taniydi.
Oliy isnod – rivoyat qilgan roviylarning soni boshqa isnodga qaraganda oz boʻlishi.
Nozil isnod– bir hadisni rivoyat qilgan roviylarning sanaddagi soni xuddi shu hadisni rivoyat qilgan boshqa sanaddan koʻpayib ketgan boʻlishi.
Muvofaqa – musanniflardan birining shayxiga uning yoʻlidan boshqa, uning yoʻli bilan rivoyat qilgandagidan kamroq adad bilan yetib borishi.
Musava – roviyni mashhur kitoblarning isnodidan boshqa isnod topishi va ikki isnod kuch va son jihatidan barobar boʻlishi.
Musofaha – isnod adadining (sanaddagi roviylar sonining) birinchi roviydan shu sanadning oxirigacha bir musannif shogirdining isnodi bilan bir xil boʻlishi.
Musalsal – hadisning roviylari sanaddagi roviylarning yohud rivoyatning sifati yoki holatini birin–ketin takrorlab kelishlari.
Aqron – yoshi teng, isnodi bir xil boʻlib, bir–biriga yaqin boʻlgan odamlar.
Mudabbaj hadis– hamma tarafdan oʻxshash boʻlgan ikki tengdosh kishilarning bir–birlaridan qilgan rivoyatlari.
Sobiq va lohiq – vafot tarixlarida katta farq boʻlgan, lekin bir shayxdan rivoyat qilgan ikki kishi.
Abodila – ismi Abdulloh boʻlgan kishilar.
Muhazramun – johiliyat va Nabiy sollallohu alayhi vasallamning zamonlarida yashab, musulmon boʻlgan, lekin Rasululloh sollallohu alayhi vasallamni koʻrmagan kishilar.
Muttafiq – roviylarning ismlari bir–biriga oʻxshash kelishi, ularning otalarining ismlari ham muvofiq boʻlishi, bu holat yozishda ham bir xil, talaffuzda ham bir xil boʻlib, shaxslari turlicha boʻlishi.
Muʼtalif – roviylarning ismlari, laqablari, kunyalari va nasablarining yozuvda bir xil boʻlishi
Muxtalif – roviylarning ismlari, laqablari, kunyalari va nasablarining oʻqishda har xil boʻlishi.
Muhmal – ismlari, otalarining ismlari yoki ismi ham, otasining ismi ham bir xil boʻlgan ikki kishidan hadis rivoyat qilib turib, ularni bir–biridan ajratib turadigan xususiyatlarini aytmay ketish.
«Undan bir kishidan ortiq odam rivoyat qilmagan roviylar «vuhdon» deyiladi».

@islomuz_quron_bot</b>  
"""

    await mes.answer(text1)
    await mes.answer(text2)
    await mes.answer(text3)


# 3 Muhaddislar
@dp.message_handler(text="Muhaddislar")
async def muhaddis(mes: Message):
    text = """<b>Muhaddis (arabchadan — hadis rivoyat qiluvchi) — hadislarni toʻplash, saralash va sharxlash bilan shugʻullanadigan olim.
    
Muhaddislar tomonidan yaratilgan va ishonarli manbalar deya e’tirof etilgan “Al-kutub as-sitta” (“Olti kitob”) quyidagilardan iborat:

Abu Abdulloh Muhammad ibn Ismoil al-Buxoriy tomonidan yozilgan “Al-jome’ as-sahih” asari

Imom Muslim an Nishopuriy (Imom Muslim ibn al-Hajjoj) tomonidan yozilgan “As-sahih” asari

Imom ibn Moja tomonidan yozilgan “Sunan” asari

Imom Abu Dovud Sulaymon Sijistoniy tomonidan yozilgan “Sunan” asari

Imom Muhammad ibn Iso at-Termiziy tomonidan yozilgan “Aj-jami al-kabir” asari

Ahmad an-Nasoiy tomonidan yozilgan “Sunan”

@islomuz_quron_bot</b>"""

    await mes.answer(text, reply_markup=muhaddislar)


# 3.1 Al Buxoriy
@dp.message_handler(text="Imom Al Buxoriy")
async def alb(mes: Message):
    await mes.answer("""
<b>
Imom Ismoil al-Buxoriy - taniqli muhaddis olim (muhaddislik — hadislar haqidagi fan, payg‘ambarimiz Muhammad s.a.v.ning islom dini uchun xos so‘zlari va ishlari haqidagi xabarlar) va ahamiyatiga ko‘ra Qur’ondan keyingi o‘rinda turuvchi “Al Jomiy as Sahih” kitobining muallifi.

Abu Abdulloh Muhammad ibn Ismoil al-Buxoriy 810 yil Buxoroda tavallud topgan. Ma’lum bo‘lishicha, uning otasining bobosi birinchi islom qabul qilganlardan bo‘lgan.

Uning otasi muqaddas rivoyatlar baxshilaridan bo‘lgan. 5-6 yoshlaridan Ismoil Qur’on va diniy ilmlarni, xususan, hadislar o‘rganishni boshlagan. Mukammal xotira egasi bo‘lib, u o‘qiganlirini tez o‘rganib olar, so‘ngra ularni har tomonlama tahlil qilardi.16 yoshiga kelib, u o‘sha zamonlarning barcha hadis to‘plamini yoddan bilgan.

825 yil Al Buxoriy o‘z onasi va akasi Ahmad bilan birga haj safarini amalga oshirish uchun Makka va Madinaga yo‘l olishadi. Ziyoratni amalga oshirgach, onasi va akasi Buxoroga qaytib kelishadi, u esa turli musulmon davlatlari bo‘ylab sayohat qilib, o‘z davrining taniqli ustozlaridan ta’lim olgan.

Rivoyatlarga ko‘ra, u yuz minglab hadislarni to‘plab, ulardan 300 mingtasini yoddan bilgan. U hayotining 42 yilini izlarishlar bilan o‘tkazadi. Kitobi ustida ishlashni u Basrada boshlaydi va uni ko‘p yillar davomida yozadi. Uning so‘zlariga ko‘ra, kitobga 1080 ta muhaddisning hadislari kiritilgan. Hadislarning ishonchliligiga ularning kelib chiqish manbasi va har bir zanjir aniq ko‘rsatgich bo‘la oladi, zero, yetkazib beruvchining axloqiy timsoli nazarda tutilganligi, unga ishonish imkonini beradi.

Manbalardan ma’lumki, u ko‘plab kitoblar yozgan bo‘lib, ular orasida “Ta’rixi Kabir” - “Buyuk Tarix” kitobi ham bor.

“As-Sahih”ni yozgach, u Buxoroga qaytadi va barcha ilm istaganlarga ta’lim beradi, bu orqali u odamlarni savodga o‘rgatib, jamiyatga katta foyda olib keladi. Uning obro‘si shu qadar baland bo‘lganki, unga noma’lum hadis xalqda ishonchsiz hisoblangan.

O‘z irodasiga qarshi ravishda u Buxoro hukmdori Tohirid Xolid ibn Ahmad bilan nizolashib qoladi va Samarqand yoqasidagi Xartang qishlog‘iga ko‘chib o‘tishga majbur bo‘ladi, shu yerda u 870 yil vafot etgan.

@islomuz_quron_bot
</b>""")


# 3.2 Imom Muslim
@dp.message_handler(text="Imom Muslim")
async def imomm(mes: Message):
    await mes.answer("""
<b>Muslim Ibn Hajjoj, imom Muslim (817 yoki 821—Nishopur — 875) — muhaddis, imom. Imom Buxoriydan keyingi hadis ilmining bilimdoni. Fiqhdan ham yaxshi xabardor boʻlgan. Yoshligida koʻp mamlakatlarga safar qilgan, jumladan, Hijoz, Misr, Suriya, Iroqda boʻlgan. Ulamolarning qayd etishlaricha, u 300 mingdan ziyod hadisni oʻrganib chiqib, ulardan 12 mingtasini ishonchli (sahih) deb topgan va oʻzining "as-Sahih" ("Sahihi Muslim") asariga kiritgan. Toʻplam musannaf shaklida tuzilgan.

Mazmunan uni "Sahihi Buxoriy"ning oʻzginasi deyish mumkin, lekin u boshka manbalarga asoslanib yozilgan. Muslim ibn Hajjoj isnodga alohida ahamiyat bergan. Kitob 52 boʻlimdan iborat, boʻlimlarning har birida oʻziga tegishli hadislar toʻplangan (masalan, dinning 5 arkoni toʻgʻrisidagi, nikohga doir, meros qoidalariga bagʻishlangan, qurbonlikka oid, paygʻambarlar va sahobalar toʻgʻrisidagi, oxirat haqidagi, axloqqa oid va tibbiy mazmundagi hadislar). Tarixiy va biografik mazmundagi hadislar bu kitobning boy manba sifatidagi qiymatini oshiradi. "As-Sahih" kitobi shariat boʻyicha qoʻllanma vazifasini oʻtashi lozimligi nazarda tutilgan. Bu asar ahli sunna nazdida 6 ta mashhur sahih kitobning ikkinchisidir.

Muslim ibn Hajjoj bundan tashqari fiqhga oid asarlar va muhaddislarga bagʻishlangan biografik toʻplamlar yaratgan, lekin yozganlari saqlanib qolmagan, bizgacha birgina "as-Sahih" asari yetib kelgan.
</b>""")


# 3.3 At Termiziy
@dp.message_handler(text="Imom at Termiziy")
async def imomt(mes: Message):
    await mes.answer("""
<b>Buyuk allomalardan biri — mashhur muhaddis (hadis ilmi olimi) Abu Iso Muhammad at-Termiziyning to‘liq ismi Abu Iso Muhammad ibn Savra ibn Muso ibn ad-Dahhok as-Sullamiy (umrining oxirlarida ko‘zi ojiz bo‘lib qolganligidan ad-Dariyr taxallusi bilan ham atalgan) at-Termiziy bo‘lib, u hijriy hisobda 209 (milodiy 824) yilda Termizda, uncha badavlat bo‘lmagan oilada tavallud topdi. Uning yoshlik yillari Termiz shahrida o‘tib, dastlabki ma’lumotni ham shu shaharda olgan. Bolaligidan o‘ta ziyrakligi, yodlash qobiliyatining kuchliligi va noyob qobiliyati bilan o‘z tengqurlaridan ajralib turgan at-Termiziy diniy va dunyoviy fanlarni, ayniqsa, hadis ilmini alohida qiziqish bilan egallagan va bu boradagi o‘z bilimlarini muttasil oshirish uchun ko‘pgina Sharq mamlakatlarini ziyorat qilgan. Jumladan, u uzoq yillar Iroqda, Isfahon, Xuroson, Makka va Madinada yashagan.

At-Termiziy qalamiga mansub asarlarning aksariyati bizgacha yetib kelgan,

«Al-jomi’» («Ja’mlovchi»);

«Ash-shamoil an-nasaviya» («Payg‘ambarning alohida fazilatlari»);

«Al-ilal fi-l-hadiys» («Hadislardagi og‘ishishlar»);

«Risola fi-l-xilof va-l-jadal» («Hadislardagi ixtilof va bahslar haqida risola»);

«At-tarix» («Tarix»);

«Kitob az-zuhd» («Taqvo haqida kitob»);

«Kitob ul-asmo va-l-kuna» («Ismlar va laqablar haqida kitob») kabi asarlar shular jumlasiga kiradi.

At-Termiziyning asarlari ichida eng mashhuri, shubhasiz, «Al-jomi’» bo‘lib, payg‘ambar alayhissalomga doir oltita ishonchli hadislar to‘plamlaridan biridir. Ushbu asar ilmiy adabiyot va manbalarda «Al-jomi’ al-kabir» («Katta to‘plam»), «Al-jomi’ us-sahiyh» («Ishonchli to‘plam»), «Jomi’at-Termiziy» («Termiziy to‘plami»), «Sunan at-Termiziy» («Termiziy sunnatlari») nomi bilan ham atalib, payg‘ambar alayhissalom hayoti va faoliyatiga doir muhim manbalardan hisoblanadi.

O‘z davrining yetuk muhaddis olimi sifatida tanilgan at-Termiziy ko‘pdan-ko‘p shogirdlarga ustozlik qilgan. Hadis ilmidagi uning shogirdlaridan Makhul ibn al-Fadl, Muhammad ibn Mahmud, Anbar, Hamad ibn Shokir, Abd ibn Muhammad an-Nasafyun, al-Haysam ibn Kulayb ash-Shoshiy, Ahmad ibn Yusuf an-Nasafiy va Abul-Abbos Muhammad ibn Mahbub al-Mahbubiylarni sanab o‘tish mumkin. U 279 hijriy (milodiy 892) yilda Termizdan uzoq bo‘lmagan Bug‘ qishlog‘ida vafot etadi va shu yerda dafn qilinadi.
</b>""")



# 3.4 Abu Dovud
@dp.message_handler(text="Abu Dovud")
async def abudovud(mes: Message):
    text = """<b>Abu Dovud Sulaymon ibn Ash'as ibn Ishoq al-Azdiy Sijistoniy hujjat bilan hukm qiluvchi, huffoz- larning sayyidi, hadislarni tahlil etuvchi «Kitobi Sahih» deb tan olingan olti muhaddisning biridurlar. Nisbatlari Basra qishloqlarining biri bo'lgan Sijistongadir.

Bu zot hijratning 202 yili Basrada tavallud topdilar. Hadislarni to'plashda Iroq, Xuroson, Shom, Misr, Arabiston Jazirasi kabi yurtlardagi ulamolar huzurida bo'lib chiqdilar. 221 hijriy sanada Kufaga safar qildilar va ana shu erdagi kishilardan ham hadislarni eshitib rivoyat qildilar.

Ulamolar bu zotda bo'lgan sifatlarni ko'p zikr qilishadi. Amr ibn Ali Bohiliy: «Imom Abu Dovud duosi ijobat bo'luvchi kishilardan edilar»-deb aytadilar. Muhammad ibn Sa'd Zuhariy: «Bu zot obid, taqvoli, fozil, solih, pok kishilardan edilar»-deb aytadilar. Abu Hotim ar-Roziy: Bu zotdek tazarru'li va bu kishidek hujjati ishonchli kishini ko'rmaganman»- deganlar.

Abu Dovudning «Sunan» kitoblari to'g'risida ham ulamolar g'oyatda maqtov fikrlar bildirishgan: Zakariyo Soniy aytadilar: «Kitobulloh Islomning asli, «Sunani Abu Dovud» Islomning ahdidir». Ulug' zotlardan Xattobiy: «Bu kitob ikkita sahih kitobdan ko'ra faqihroq va hadis ilmida buning singari kitob tasnif etilmagan»-deb aytadilar.

Imom Abu Dovud hammasi bo'lib 50000 hadis rivoyat qilib, bulardan 4800-ta sahih hadisni «Sunan» kitoblariga kiritdilar. Imom Abu Dovudning «Sunan» kitoblariga ko'plab sharh va muxtasarlar yozildi. Bu zot hadislarni Muslim ibn Ibrohim, Sulaymon ibn Xarb, Abu Umar Havziy, Abu Valid Tayolisiy, Abu Muammar al-Muaqqad, Abdulloh ibn Maslama al-Qa'nabiy, Ahmad ibn Hanbal, Usmon ibn Shayba, Amr ibn Avn, Hishom ibn Ammor Dimashqiy, Rabiy' ibn Nofi' Halabiy, Ahmad ibn Solih Misriy va boshqa bir nechta jamoat kishilardan eshitdilar.

Imom Abu Dovuddan Termiziy, Nasaiy, o'g'illari Abdulloh, Ahmad ibn Muhammad ibn Horun, Ali ibn Husayn ibn Abd, Muhammad ibn Muhammad ad-Davriy, Ismoil ibn Muhamad Saffor, Ahmad ibn Salmon Najjor va boshqa bir necha kishilar rivoyat qiishdi. Imom Abu Dovud hijratning 275 yili, Shavvol oyining 16-kunida Basrada vafot etdilar.

@islomuz_quron_bot</b>"""
    await mes.answer(text)



# 3.5 Nasoiy
@dp.message_handler(text="Nasoiy")
async def nasoiy(mes: Message):
    text = """
<b>
Imom, hofiz, shayxulislom Ahmad ibn Shu’ayb ibn Ali ibn Sinon ibn Bahr ibn Dinor Abu Abdulloh Xurosoniy Nasaiy hijratning 215 yili Xurosonning shaharlaridan biri bo‘lgan Nisoda dunyoga keldilar.

Bu zot kitobi “Sahih” deb tan olingan olti imomning biridurlar. As’hobi hadislar ichida asllar ahlining imomi va peshqadami edilar. Yoshlari o‘n beshga yetganda Qutayba ibn Sa’id al-Balxiyning huzurlariga borib, bir yilu ikki oy davomida hadis eshitadilar.

Imom Nasaiy ilm talab qilib Xuroson, Hijoz, Misr, Iroq, Arabiston yarim oroli, Shom kabi yurtlarni kezib chiqdilar. So‘ngra Misrda «al-Qanadiyl» nomli mashhur kitob bozori bo‘lgan tor ko‘chada yashadilar. Bu zotning huzurlariga hadis eshitish uchun huffozlar tashrif buyurishar edi. Ana shu vaqtda bu kishiga teng keladigan kishi topilmas edi. U zotning sifatlarini zikr qilib Dora Qutniy aytadilar: «Abu Abdurahmon hadis ilmida esga olinganlarning muqaddami edilar». Ibn al-Asiyr «Jomi’ ul-Usul» kitobida: «Nasaiy Shofe’iy mazhabida edilar va shu mazhabda “Haj” kitoblari bor. U kishi taqvoli, talabchan bo‘lib Dovud payg‘ambarning ro‘zasida davomli edilar», deb aytadilar. Bu zot roviylarni o‘z vaqtida jarohatlab, o‘z vaqtida ta’dil etardilar. Shuning uchun jarh va ta’dillari ulamolar orasida e’tiborlidir.

Imom Nasaiy ta’lif etgan kitoblari quyidagilar: “Sunani kubro va sug‘ro”, «Xasoisu fiy fazli Ali ibn Abu Tolib va oli bayt», «Kitobu zuafo val matrukiyn», “Manosiku Nasaiy”, «Jam’u musnad Molik ibn Anas va musnad Ali ibn Abu Tolib».

Imom Nasaiyning «As-Sunan al-Kubro» kitoblari avvaliga ko‘pgina zaif hadislarni ham o‘z ichiga olgan edi. Keyin esa, zaif hadislarni olib tashlab, sahihlarini qoldirganlar va bu kitoblarini «Al-Mujtaba’» deb nomlaganlar.

Imom Nasaiyning «Al-Mujtaba’»ni yozishlariga sabab, u kishi «As-Sunan al-Kubro» kitobini yozgach, Ramla degan joyning amiriga taqdim qilganlarida, amir: “Buning hammasi sahihmi?” deb so‘ragan. Imom: “Bunda sahih ham, hasan ham bor”, dedilar. Shunda amir sahihlarini ajratishni so‘radi. Shu munosabat bilan Imom Nasaiy «As-Sunan al-Kubro» kitoblaridan sahih hadislarni tanlab «Al-Mujtaba’» yoki “As-Sunan as-sug‘ro” deb nomlangan kitobni yozdilar.

Bu kitob oltita “Sahih” deb nomlangan kitobning biridir. U birinchi marta 1256 hijriy sanada Hindistonda chop etilgan va eng ishonchli hadis kitoblaridan hamda hadis ulamolari tarafidan zaif hadislari eng kam va majruh kishilari yo‘q kitoblardan deb tan olingan. Bu o‘rinda Abu Dovud va Termiziy hadislariga solishtiriladi. Shuningdek, bu kitob hadislarni bir o‘rindagina keltirishga, zarurat tug‘ilgandagina boshqa joyda rivoyat qilishga ehtimom qiladi. Shu vaqtning o‘zida hadislardan fiqh hukmlarini, illatlari bayoni bilan chiqarishga e’tibor beradi.

Imom Nasaiy kitoblariga ko‘plab sharhlar yozilgan. Bu zotning ustozlari esa quyidagilardir: Ahmad ibn Abdata az-Zabyi, Ahmad ibn Maniy’, Bashir ibn Muoz al-Aqdiy, Hasan ibn Saboh, Muhammad ibn Ismoil ibn Ayla Dimashqiy, Muhammad ibn Abbon al-Balxiy, Ali ibn Hojar, Amr ibn Zirorata al-Kalbiy, Iso ibn Muhammad ar-Ramliy, Muhammad ibn Hoshim al-Ba’labakkiy, Is’hoq ibn Shohiyn, Qutayba ibn Said, Is’hoq ibn Ibrohim, Is’hoq ibn Mansur, Is’hoq ibn Muso al-Ansoriy, Ibrohim ibn Said al-Javhariy, Ibrohim al-Javjoniy, Iso ibn Hammod, Hishom ibn Ammor va boshqalardir.

Imom Nasaiydan Ahmad ibn Umayr ibn Javso, Muhammad ibn Ja’far ibn Mallas, Abulqosim ibn Abul Aqb, Abul Maymun ibn Rashid, Abu Ali at-Tabaroniy, Abu Ja’far at-Tahoviy va boshqalar rivoyat qilishgan.

Bu zot tavallud topgan Niso shahri haqida ma’lumot: Shaharning Niso deb atalishiga sabab: fotihlar Xurosonni fath etishganda shahar erkaklari qochib ketishgan ekan. Musulmonlar shaharda erkak zotini topa olmay, uni tashlab o‘tib ketishgan ekan. Shu sababli u Niso («Ayollar») shahri, deb atalgan ekan. U hozirgi Turkmaniston yerlarida joylashgan shahardir. Bu yerdan Imom Nasaiydan tashqari Abu Ahmad Homid Zinjaviy al-Azdiy kabi katta olimlar ham chiqqan.

Imom Nasaiy hijratning 303 yili Makkada shahid bo‘ldilar va Safo-Marva orasiga dafn etildilar.

@islomuz_quron_bot
</b>"""
    await mes.answer(text)



# 3.6 Ibn Moja
@dp.message_handler(text="Ibn Moja")
async def ibnmoja(mes: Message):
    text = """<b>Abu Abdulloh Muhammad ibn Yazid ibn Abdulloh ibn Moja Robiiy al-Qazviniy hijratning 209 yili Iroq shaharlaridan biri – Qazvinda tavallud topdilar. Otalari Robia qabilasining boshligʻi boʻlib, Moja ismi bilan tanilgan edilar.

Imom Ibn Moja «Sahih» deb tan olingan 6 ta kitobdan birining sohibi boʻlmish imomlardan edilar.

U zot voyaga yetganda hadis toʻplash uchun Iroq, Basra, Kufa, Shom, Misr, Ray kabi oʻlkalarga safar qildilar. Damashqdagi Hishom ibn Ammor, Abbos ibn Valid, Abdulloh ibn Ahmad ibn Bashir, Mahmud ibn Xolid, Misrdagi Harlamata ibn Yahyo, Abu Tohir ibn as-Sirota, Muhammad ibn Ramh, Muhammad ibn Horis, Yunus ibn Abdulaʼlo, Xumsdagi Muhammad ibn Musaffo, Hashshom ibn Abdulmalik, Bagʻdoddagi Abu Bakr ibn Abu Shayba, Ahmad ibn Abda, Ismoil ibn Muso, Abu Haysama Zohir ibn Xarb kabi ulamolardan dars olib, hadislar toʻpladilar.

Imom Ibn Moja 32 ta kitob yozganlar. Shulardan mashhurlari: «Sunani Ibn Moja» (hadis kitoblari), «Tafsiri Ibn Moja» (tafsir kitoblari), «Tarixi Ibn Moja» (tarix kitoblari).

U zotdan Muhammad Iso al-Abhariy, Abu Umar Ahmad ibn Muhammad al-Madaniy, Ali ibn Ibrohim al-Qatton, Sulaymon ibn Yazid al-Foliy, Abu Toyyib Ahmad ibn Ruh al-Bagʻdodiylar dars olishgan va hadis rivoyat qilishgan.

Ibn Mojaning oʻzlari va kitoblari toʻgʻrisida ulamolar koʻp maqtovli soʻzlarni aytishgan. Abu Yaʼlo al-Halimiy aytadilar: «Ibn Mojaga odamlar ishonib, hadis ilmida u kishiga suyanadilar». Muhammad ibn Jaʼfar al-Kattoniy oʻzlarining «Risolati al-mustatrofa» kitoblarida shunday keltiradilar: «Ulamolar Ibn Mojaning «Sunan» kitoblarini ishonchli, kuchli va fiqh ilmida katta foyda berishini koʻrib, oltinchi sahih kitob, deb tan olishdi».

Ibn Tohir aytadilar: «Kimki Ibn Mojaning hadis kitoblariga qarasa, boblari koʻpligi, bir hadis qayta takrorlanmasligi va hadislarning chiroyli tartibda yozilganligini koʻrib, haqiqatda u zotni hadis jamlashda va kitob yozishda qanday yaxshi yoʻl tutganlarini biladi. Bu kitob juda mashhur boʻlmasa ham, oʻziga yarasha obroʻ-eʼtibori bordir».

Abu Hasan Ali Ibrohim ibn Salama aytadilar: «Imomning «Sunan» kitobi 32 juz boʻlib, unda 1500 ta bob bordir. Va bu kitob 4341dan koʻproq hadisni oʻz ichiga olgandir».

Imom Ibn  Moja hijratning 273 yili vafot etdilar.

@islomuz_quron_bot</b>"""
    await mes.answer(text)





# 4 Islomning madori bo'lgan hadislar
@dp.message_handler(text="Islomning madori bo'lgan hadislar")
async def islomningmadori(mes: Message):
    text = """
<b>Imom Abu Dovud rahmatullohi alayhi: «Insonning dini uchun toʻrtta hadis kifoya qilur: 
1. «Albatta, amallar niyatga bogʻliqdir» degan hadis. 
2. «Birortangiz toki oʻziga yaxshi koʻrgan narsani oʻz birodariga ham yaxshi koʻrmaguncha moʻmin boʻla olmaydi» degan hadis. 
3. «Kishi Islomining goʻzal boʻlishi oʻzi uchun behuda boʻlgan narsani tark qilishidir» degan hadis. 
4. «Albatta, halol ochiq-oydindir, harom ochiq-oydindir» degan hadis», degan ekanlar.
Quyida shu hadislarning sharhlari kelgan:</b>
@islomuz_quron_bot"""
    await mes.answer(text, reply_markup=hadis4)


@dp.message_handler(text="1-hadis")
async def birh(mes: Message):
    text = """
<b>Umar roziyallohu anhudan rivoyat qilinadi: 

«Paygʻambar sollallohu alayhi vasallam: «Albatta, amallar niyatga bogʻliqdir. Albatta, har bir kishiga niyat qilgan narsasi boʻladi. Bas, kimning hijrati Alloh va Uning Rasuli uchun boʻlsa, uning hijrati Allohga va Uning Rasuliga boʻladi. Kimning hijrati dunyo uchun boʻlsa, unga erishadi. Yoki ayol uchun boʻlsa, uni nikohlab oladi. Bas, uning hijrati nima uchun qilgan boʻlsa, oʻshanga boʻladi», dedilar».

Beshovlari rivoyat qilishgan.

Sharh: Bu hadisi sharif hazrati Umar roziyallohu anhudan rivoyat qilinmoqda. U kishi bilan yuqorida tanishib oʻtganmiz.
Paygʻambarimiz sollallohu alayhi vasallam oʻzlarining hadislarida qisqa iboralar bilan bir olam maʼnoni bayon qilganlar. Shuning uchun ham ulamolarimiz bu hadisi sharifni alohida eʼtibor bilan, atroflicha oʻrganib chiqqanlar.
Imom Ahmad ibn Hanbal rahmatullohu alayhi: «Ilmning uchdan biri shu hadisda», degan ekanlar.
Chunki, bandaning savob kasb qilishi uch narsa; dil, til va badan orqali boʻladi. Bu hadisda dil orqali boʻladigan narsa toʻla bayon qilingan. Chunki, din ichki va tashqi amallardan iboratdir. Ichki amal niyatdan iborat, niyat esa qalb ila boʻladi.

Endi hadisi sharifni batafsil oʻrganib chiqaylik:
«Albatta, amallar niyatga bogʻliqdir».
Yaʼni, har bir amal niyatga qarab baholanadi. Til bilan bajaraladigan amalmi, badan bilan bajariladigan amalmi yoki farzmi, vojibmi, sunnatmi, naflmi-hammasining toʻgʻri boʻlishi niyatga bogʻliqdir. Shariat hukmi boʻyicha niyat bilan qilinmagan amal-amal hisoblanmaydi.
«Albatta, har bir kishiga niyat qilgan narsasi boʻladi».
Nimani niyat qilsa oʻsha niyatidagi narsaga erishadi. Peshin namozini farzini oʻqiyapman, deb niyat qilsa, oʻsha namozning savobini oladi. Nafl roʻza tutayapman, deb niyat qilsa, nafl roʻzaning savobini oladi.
«Bas, kimning hijrati Alloh va Uning Rasuli uchun boʻlsa, uning hijrati Allohga va Uning Rasuliga boʻladi».
«Hijrat» lugʻatda biror narsadan ajrash, uning hijronida qolishni anglatadi.
Shariatda esa, Alloh va Uning Rasuli roziligini tilab, dinu diyonat yoʻlida Makkani tark etib, Madinaga borishga aytilgan. Keyinchalik esa dinu diyonat yoʻlida oʻz vatanini tashlab, boshqa yurtlarga koʻchib ketishni «hijrat» deyilgan.
Demak, Alloh va Uning Rasuli uchun, degan niyat bilan hijrat qilgan odam haqiqiy muhojir boʻladi. Alloh taolo va Paygʻambar sollallohu alayhi vasallam tomonidan muhojirlarga vaʼda qilingan martabalarga erishadi.
«Kimning hijrati dunyo uchun boʻlsa, unga erishadi». 
Molu dunyo qasdida, unga erishish niyatida hijrat qilgan boʻlsa, unga erishadi.
«Yoki ayol uchun boʻlsa, uni nikohlab oladi».
Ummu Qaysni nikohlab olgan kishiga oʻxshab niyatiga yetadi.
«Bas uning, hijrati nima uchun qilgan boʻlsa, oʻshanga boʻladi».
Yaʼni molu dunyo va ayoldan boshqa narsani, misol uchun doʻst ortdirish, sayohat qilish, davlat qurishga tayyorlanish, kasb oʻrganish va yana boshqa narsalarni niyat qilgan boʻlsa, oʻsha narsasi uchun boʻladi.
Manba: https://islom.uz/maqola/757

@islomuz_quron_bot</b>
"""
    await mes.answer(text)


@dp.message_handler(text="2-hadis")
async def ikkih(mes: Message):
    text = """
<b>Anas ibn Molik roziyallohu anhu rivoyat qiladi:

“Rasululloh alayhissalotu vassallom aytadilar: “Sizlarning biringiz haqiqiy iymonga erisha olmaydi, toki o‘zi uchun yaxshi ko‘rgan narsani birodari uchun yaxshi ko‘rmaguncha”.

Imom Buxoriy va Imom Muslim rivoyati.

Bu hadis nafaqat musulmon jamiyatini, balki butun insoniy jamiyat odobini, axloqini, o‘zaro munosabatini eng go‘zal shaklda shakllantirib beradigan, tartibga solib beradigan axloqlarni o‘z ichiga jamlagan hadislardan biridir. 

Ushbu hadisdan olinadigan bir qancha xulosalar bor. Inson odatda tabiatan yaratilishda o‘zining manfaati uchun urinishga, harakat qilishga moyil qilib yaratilgan. Shu e'tibordan ishga boradi, harakat qiladi, safar qiladi, qiyinchiliklarga uchraydi. Endi mana shu manfaat uchun, o‘zining foydasi uchun harakat qilishda dinimiz ma'lum bir mezonlarni belgilab bergan. Manfaat deb jinoyatga qo‘l urish, harom narsalarni kasb qilish, birovning haqini yeyish mumkin emas.

Inson o‘ziga savol berishi kerak: “Men o‘zim uchun nimalarni foydali deb bildim?” Avvalo, moddiy narsadan kelib chiqmasligimiz kerak. Ma'naviy nuqtadan kelib chiqaylik. Masalan, barcha o‘zini ilmli, axloqi yuqori, o‘zgalardan ma'naviy ustun bo‘lishini istaydi. Ana shu o‘zi uchun istagan narsani atrofdagi musulmon birodarlariga ham istasa, o‘zi uchun yaxshi ko‘rgan narsani boshqalarga ham ravo ko‘rgan bo‘ladi.
Ikkinchi ma'noda moddiy manfaatlar ham turadi.
Alloh taolo Oli Imron surasining 92-oyatida: “Suygan narsalaringizdan ehson qilmaguningizgacha sira yaxshilikka (jannatga)erisha olmaysizlar.Nimaniki ehson qilsangiz, albatta, Alloh uni biluvchidir.”, deb marhamat qiladi.
@islomuz_quron_bot</b>
"""
    await mes.answer(text)


@dp.message_handler(text="3-hadis")
async def uchh(mes: Message):
    text = """
<b>Abu Hurayra roziyallohu anhudan rivoyat qilinadi:
«Nabiy sollallohu alayhi vasallam:
«Kishi Islomining husni - behuda narsalarni tark qilishidadir», dedilar».
Termiziy va Ibn Moja rivoyat qilishgan.

Ushbu hadisda Paygʻambarimiz ummatlarga qisqa soʻz bilan goʻzal xulqni oʻrgatmoqdalar. Banda bu bilan dunyo yaxshiliklari va oxirat saodatiga erishadi. Olimlar: “Rasululloh muborak hadislarida islom dinining yarmini ifodaladilar. Chunki din solih amalni bajarish va gunohni tark qilishdan iborat. Mazkur hadis yomonlik va manfaati yoʻq amallarni tark qilish lozim ekaniga dalildir”, deyishadi.

Darhaqiqat, kishilarning behuda narsalarga berilib ketishi baxtsiz boʻlishning asosiy omilidir. Imom Shofeiy (rahmatullohi alayh) aytadi: “Insonning aqli uch narsa bilan ziyoda boʻladi. Olimlarning suhbatida boʻlish, yaxshilar bilan birga oʻtirish va behuda soʻzni tark qilish”. Qurʼoni karimda bunday marhamat qilinadi: “Moʻminlar najot topdilar… Ular behuda (soʻz va ishlar)dan yuz oʻgiruvchidirlar”.

Foydasiz narsalar bilan shugʻullanish insonning iymoni zaif ekaniga ishoradir. Odam dunyoda yasharkan, atrofida turli kishilar va har xil mashgʻulotlarga duch keladi. Inson atrofidagi barcha bilan aloqa qilaversa, foydasiz ishlar bilan shugʻullanaversa, zimmasidagi asosiy vazifa, burch va majburiyatlarini bajara olmaydi. Buning natijasi esa yaxshi boʻlmaydi. Qurʼoni karimda bunday marhamat qilinadi: “(Ey inson!) Oʻzing (aniq) bilmagan narsaga ergashma! Chunki quloq, koʻz, dilning har biri toʻgʻrisida (har bir inson) masʼul boʻlur (javob berur)” (“Isro” surasi, 36-oyat).

Har bir kishi aytgan soʻzi, oʻtkazgan soniyasidan soʻraladi. Vaqtni zoye qilib, lagʻv soʻzlarni gapirib umr oʻtkazganlar najot topmaydi. Anas ibn Molik (roziyallohu anhu)dan rivoyat qilinadi: “Bir sahoba vafot etdi. Bir kishi: “Jannat muborak boʻlsin”, dedi. Rasululloh (sollallohu alayhi va sallam): “Unday dema! Sen bilmaysan, balki, u behuda soʻzlarni gapirgandir”, dedilar” (Imom Termiziy rivoyati).

Manfaatli yumush bilan band boʻlish salomatlik va najot yoʻlidir. Inson zimmasidagi majburiyatlarini bilsa va masʼuliyatini his etsa, u oʻzini shu ish bilan band qiladi. Shuningdek, dunyo va oxiratda baxtli boʻlishiga sabab boʻladigan ishga mashgʻul boʻladi, ortiqcha narsalarni tark qiladi. Luqmoni Hakim (rahimahulloh)dan “Bunday fazilatga yetishishingizga nima sabab boʻldi?”, deb soʻrashganida “Foydasiz narsalarni tark qilish”, deb javob bergan ekan.

Agar kishi foydali ish bilan band boʻlsa, yomonlik va gunohlardan tiyiladi. Natijada xulqi goʻzal, iymoni mustahkam va taqvosi quvvatli boʻladi. Bu haqda Paygʻambarimiz (sollallohu alayhi va sallam): “Kim dinini goʻzal qilsa, bajargan bitta yaxshi amali oʻntadan yetti yuztagacha koʻpaytirib yoziladi”, deganlar” (Imom Buxoriy rivoyati).

Manbalarda taom, ichimlik, kiyim, yashash joyi kabi inson hayoti uchun zarur ashyolar hamda dunyo va oxiratda salomat boʻlishiga bogʻliq ishlar foydali amallar sirasiga kirishi zikr qilinadi. Bundan boshqa narsalar behudadir. Demak, inson hojatidan tashqari dunyoviy maqsadlarning keragi yoʻq. Jumladan, ortiqcha boyishni orzu qilish, mansab xohlash, boshqalarning maqtovini yaxshi koʻrish kabilardan saqlanish foydalidir. Alloh taolo bunday marhamat qiladi: “Siz (kofirlardan ayrim) toifalarni sinashimiz uchun bahramand qilgan dunyo hayoti goʻzalliklaridan iborat narsalarga koʻzlaringizni termultirmang! Rabbingizning rizqi yaxshiroq va boqiyroqdir” (“Toho” surasi, 131-oyat).

Shu bilan birga, kishiga manfaati yoʻq turli oʻyinlar, hazil-mutoyiba kabi muboh amallar ham foydasizdir. Moʻmin-musulmonlar bunday ishlarni tark qilishlari goʻzal xulq sanaladi. Chunki mazkur ishlar bebaho vaqtni zoye ketkizadi. Hasan Basriy (rahmatullohi alayh) aytadi: “Bandaning behuda narsalar bilan band boʻlib qolishi undan Alloh taolo yuz oʻgirganining belgisidir”.

Bundan koʻrinadiki, foydali ish bilan band boʻlish bandani Alloh taologa yaqin qiladi. 
Abu Hurayra roziyallohu anhudan rivoyat qilinadi: “Nabiy sollallohu alayhi va sallam: “Foydali narsaga haris boʻlgin”, dedilar”
Manba: islom.uz

@islomuz_quron_bot</b>
"""
    await mes.answer(text)


@dp.message_handler(text="4-hadis")
async def torth(mes: Message):
    text = """
<b>Noʻmon ibn Bashir roziyallohu anhu rivoyat qiladi: 

“Men Rasululloh sollallohu alayhi vasallamning: “Halol aniq, harom aniq. Ammo ularning oʻrtasida shubhali narsalar bor. Koʻp odamlar uni bilmaydilar. Kim shubhali narsalardan saqlansa, dini va obroʻsini saqlabdi. Kim toʻsiq atrofidagi choʻponga oʻxshab shubhali narsalarga oʻralashib qolsa, unga tushib qoladi. Ogoh boʻlinglarki, har bir podshohning chegarasi boʻladi. Allohning Yerdagi chegarasi U Zot harom qilgan narsalardir. Ogoh boʻlinglarki, tanada bir parcha goʻsht bor. Agar u tuzalsa, butun tana tuzaladi. Agar u buzilsa, butun tana buziladi. Ogoh boʻlinglarki, u qalbdir”, deganlarini eshitganman”

Buxoriy, Muslim, Sunan sohiblari, Ahmad, Dorimiy, Ibn Hibbon va Bayhaqiy rivoyati.

Hadis sharifda kim oʻzini shubhali narsalardan ehtiyot qilsa, dinini nuqsondan, oʻzini taʼna va dashnomlardan saqlagan boʻladi deyilmoqda. Bu qoidaga halol kasb-hunar qilishga alohida eʼtibor berish kerak. Shunda banda qalbi sogʻlom, imoni mustahkam boʻladi.

Imom Navaviy aytadi: “Narsalar uch qismga boʻlinadi: halol ochiq-oydin, uning joizligida shubha yoʻq. Bularga non, mevalar, yogʻ, asal, goʻshti isteʼmol qilinadigan hayvon suti va tuxumi, bundan boshqa taomlar kiradi. Shuningdek, gapirish, nazar solish, yurish va shu kabi tasarrufotlar ham halol. Bu ishlarning halolligiga shubha yoʻq.

Harom narsalarga xamr, toʻngʻiz goʻshti, oʻlimtik, bavl va oqqan qon, shuningdek, zino, yolgʻon, gʻiybat, boʻhton, nomahramlarga nazar solish va shu kabilar kiradi.

Shubhali narsalar shuki, Qurʼon, sunnat va ijmoʼda biron narsa deyilmagan boʻlsa, mujtahid ijtihod qiladi. Halol yoki haromligi nomaʼlum narsalarni tark qilish taqvodir. Rasululloh sollallohu alayhi vasallamning “kim shubhali narsalarni tark qilsa, dini va obroʻsini saqlab qoladi”, degan hadislariga muvofiqdir” (Sharhun navaviy ʼala sahihi Muslim).

Hadisda harom bilan halol oʻrtasidagi toʻsiq podshohning chegarasiga oʻxshatilmoqda. Har bir hukmdorning odamlar kirishiga toʻsqinlik qiladigan chegarasi boʻladi. Agar biron kishi undan oʻtib ketsa, jazolanadi. Xuddi shuningdek, hukmdorlar hukmdori, olamlar Parvardigori Allohning oʻz chegaralari, oʻtilishi mumkin boʻlmagan hududlari bor. Bu harom narsalar va ishlardir. Kim bu chegara yaqiniga kelsa, undan oʻtib ketish xavfi tugʻiladi. Shu sabab ham bu chegara yaqiniga kelmaslik shart.
Manba: http://old.muslim.uz/

@islomuz_quron_bot</b>
"""
    await mes.answer(text)

    # 5 hadisi qudsiylar


@dp.message_handler(text="Hadisi Qudsiy")
async def hq(mes: Message):
    text = """<b>«Ey Odam farzandi! 
Qoʻlingni koʻkraging ustiga qoʻy. Nimaniki oʻzing uchun yaxshi koʻrsang, oʻzingdan boshqasi uchun ham uni yaxshi koʻr. 

Ey Odam farzandi! 
Taning zaif, tiling yengil, qalbing esa zolimdir. 

Ey Odam farzandi! 
Oxirgi chegara oʻlim, oʻlim kelishidan oldin amal qilib qol. 

Ey Odam farzandi! 
To rizqini ham yaratmaguncha, birorta aʼzongni yaratmadim. 

Ey Odam farzandi! 
Agar seni soqov qilib yaratganimda til uchun, koʻr qilib yaratganimda koʻz uchun, kar qilib yaratganimda quloq uchun hasrat chekkan boʻlarding. Bas, bergan neʼmatimning qadriga yet, Menga shukr qil, kufr keltirma, chunki Menga qaytajaksan. 

Ey Odam farzandi! 
Senga taqsimlab qoʻygan narsam talabida oʻzingni qiynama. Senga taqsimlagan har bir narsam to tugagunicha, oʻzi seni talab qilib boradi. 

Ey Odam farzandi! 
Meni oʻrtaga qoʻyib yolgʻon qasam ichma. Kim Mening nomim bilan yolgʻon qasam ichsa, doʻzaxga kiritaman. 

Ey Odam farzandi! 
Bergan rizqimni yeganingdan soʻng toatimga kirish. 

Ey Odam farzandi! 
Mendan ertaning rizqini soʻrama, chunki Men ham sendan ertaga qiladigan amalingni (bugun) talab qilayotganim yoʻq-ku! 

Ey Odam farzandi! 
Men sening ozgina amalingga roziman. Sen esa bergan koʻp rizqimga ham rozi emassan. 

Ey Odam farzandi! 
Agar dunyoni bandalarimdan birortasiga qoldirganimda albatta uni paygʻambarlarimga qoldirgan boʻlardim, ular (shu dunyo orqali) bandalarimni toatimga va buyruqlarimni bajarishga chaqirgan boʻlardilar. 

Ey Odam farzandi! 
O'lim senga tushishidan oldin oʻzing uchun amal qil. Xato(lar) seni aldab qoʻymasin. Chunki (hali) xatolar izidan yurish bor. Hayot va uzun orzu-havaslar seni tavbadan chalgʻitmasin. Negaki, tavbani kechiktirganing uchun pushaymon foyda bermaydigan kunda pushaymonlar ichra qolasan. 

Ey Odam farzandi! 
Senga rizq etib bergan moldan Mening haqqimni chiqarmasang va kambagʻallarni u moldagi haqlarini olishdan toʻssang, ustingda shunday bir zolim hukmron qilinadiki, u sendan molni tortib oladi, Men ham mol tufayli keladigan savobdan seni mahrum qilaman. 

Ey Odam farzandi! 
Agar dunyo sen tomon yuz tutsa, oʻlimni esla, agar gunohni qasd qilsang, tavbani esla, mol-dunyo qoʻlga kiritsang, hisob-kitobni esla, taomga oʻtirsang, ochlarni esla, nafsing zaifni (jazolashga) undasa, Allohning sening ustingdagi qudratini esla. Agar Alloh xohlasa, qudratini ustingda hukmron qilib qoʻyadi. Agar ustingga bir balo tushsa, «La havla vala quvvata illa billahil aliyyil ʼaziym»ni aytish bilan yordam soʻra. Agar kasal boʻlsang, nafsingni sadaqa bilan muolaja qil. Agar senga biror musibat yetsa, «Inna lillahi va inna ilayhi rojiʼun», "Albatta biz Allohning (bandalarimiz) va albatta biz u Zotga qaytguvchilarmiz" 
(Baqara, 156) degin».

Imom Gʻazzoliy “Qirq hadisi qudsiy”dan. 
@islomuz_quron_bot</b>"""
    await mes.answer(text)
    await mes.answer_document("https://t.me/islomiy_mediya/26", caption="""
Imom G'azzoliyning 40 hadisi qudsiy kitobi asosida tayyorlangan dastur

@islomiy_mediya
@islomuz_quron_bot""")


# 6 Hadislar to'plami apk lar
@dp.message_handler(text="Hadislar to'plami")
async def hadislart(mes: Message):
    await mes.answer_document("https://t.me/islomiy_mediya/19", caption="""
<b>Android tizimi uchun

“Oltin silsila” majmuasi dasturining beta versiyasi. Ushbu dasturga quyidagi sahih toʻplamlar kiradi:

1. “Sahihul Buxoriy” 8 jildlik
2. “Sahihu Muslim” (tayyorlanmoqda)
3. “Sunan Abu Dovud” (tayyorlanmoqda)
4. “Sunan Termiziy” (tayyorlanmoqda)
5. “Sunan Nasoiy” (tayyorlanmoqda)
6. “Sunan Ibn Moja” (tayyorlanmoqda)
7. “Sunan Dorimiy” (tayyorlanmoqda)
8. “Muvatto Molik” (tayyorlanmoqda)
9. “Sahih Ibn Hibbon” (tayyorlanmoqda)

Alloh taolo barchamizga Rasululloh sollallohu alayhi vasallamning muborak hadisi shariflarini oʻqish, oʻrganish va ularga amal qilish baxtini nasib aylasin!

Kitobni harid qilish uchun: @HilolNashr

@islomiy_mediya
@islomuz_quron_bot  </b>""")
    await mes.answer_document("https://t.me/islomiy_mediya/20", caption="""
<b>
Android tizimi uchun

Ushbu kitob buyuk Vatandoshimiz Imom al-Buxoriyning “Al-jome’ as-sahih” asarining o‘zbek tilidagi tarjimasi hisoblanadi.

Imom al-Buxoriy “Al-jome’ as-sahih” (Ishonchli to‘plam) kitobi ustida 16 yil ishlagan bo‘lib, unga kiritilgan 7397 hadis 600 ming hadisning ichidan saralanib olingan.

@islomiy_mediya
@islomuz_quron_bot
</b>""")
    await mes.answer_document("https://t.me/islomiy_mediya/21", caption="""
<b>
Sunani Termiziy 
Hadislar to'plami

@islomiy_mediya
@islomuz_quron_bot
</b>""")

    await mes.answer_document("https://t.me/islomiy_mediya/22", caption="""
<b>
Imom Navaviyning Arbain asari

“Arbain Navaviy” – mashhur muhaddis, imom Abu Zakariyo Yahyo ibn Sharaf An-Navaviy Ash-Shofi’iy (631-676 hijriy/1233-1277 milodiy) rohmatullohi alayh tartib bergan hadislar to‘plami. Bu to‘plamda 42 ta hadis bo‘lishiga qaramay “Arba’un” – “Qirq” deb nomlangan. Chunki arablarda kichik sonlarni o‘ziga yaqin yirik sonlarga yaxlitlash odati bor.Bu hadislarning har biri (alohida tarzda) dinning eng muhim qoidalaridan biri sanaladi. Olimlar (men tanlab olgan) bu hadislarni «Islomdagi asos-tayanch boʻladigan», «Islomni namoyon qiladigan», «Uning uchdan biriga teng keladigan hadislar», deb taʼriflashgan».

@islomiy_mediya
@islomuz_quron_bot</b>""")
    await mes.answer_document("https://t.me/islomiy_mediya/23", caption=
    """
    <b>
    Alloh Taolo barchamizni mazkur dasturda jamlangan Paygʻambarimiz Muhammad alayhissalomning muborak hadislaridan bahramand boʻlishimizni va ularga amal qilmogʻimizni nasib aylasin. (Omin)
    
    @islomiy_mediya
    @islomuz_quron_bot
    
    </b>
    """)
    await mes.answer_document("https://t.me/islomiy_mediya/24", caption=
    """
    <b>
    Dasturdagi hadislar ro'yxati:
    
    - Jannatga yaqinlashtiruvchi amal
    - Tahorat olib yotishning 6 fazilati
    - Jannat xushxabari berilgan kishilar va amallar
    - Haj va umra savobiga teng ibodat
    - Yengil, ammo savobi ulugʻ amallar
    - Hadis sharhi: Mol – dunyo fitnami?
    - Sunnat va hadisning farqi
    - Sunnatlarning onasi
    - Imom nasaiy
    - Imom Dorimiy
    - Kasbingiz halol boʻlsin!
    - Jannatga kirishni hohlaysizmi?
    - Bir hadis sharhi
    - Sahihul Buxoriy
    - Bir hadis uchun bir yil
    
    @islomiy_mediya
    @islomuz_quron_bot
    </b>
    """)
    await mes.answer_document("https://t.me/islomiy_mediya/25",
                              caption="""
<b>
Imom Muslimning hadislari

Xatolik va kamchiliklari bo'lsa uzr so'raymiz

@islomiy_mediya
@islomuz_quron_bot
</b>""")
