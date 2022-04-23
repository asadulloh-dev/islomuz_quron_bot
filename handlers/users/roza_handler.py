from loader import dp

from aiogram.types import Message
from keyboards.default.roza_keyboard import roza


@dp.message_handler(text="☪ Ro'za")
async def ramazan_png(mes: Message):
    # await mes.answer("Ramazon taqvimi 2021")
    await mes.answer("Ro'za bo'limi", reply_markup=roza)


@dp.message_handler(text="Ramazon 2022")
async def ramazon2022(mes: Message):
    await mes.answer("Ramazon taqvimi 2022\n"
                     "Manba:namozvaqti.uz")
    await mes.answer_photo("https://t.me/alquranuz/3085", caption="<b>Toshkent vaqti bilan\n@Hidoyat_taqvim_bot\n@islomuz_quron_bot</b>")
    await mes.answer_photo("https://t.me/IT_info_chat/159", caption="<b>Namangan vaqti bilan\n@islomuz_quron_bot</b>")
    await mes.answer_photo("https://t.me/IT_info_chat/160", caption="Farg'ona vaqti bilan\n@islomuz_quron_bot")
    await mes.answer_photo("https://t.me/IT_info_chat/161", caption="Andijon vaqti bilan\n@islomuz_quron_bot")
    await mes.answer_photo("https://t.me/IT_info_chat/162", caption="Sirdaryo vaqti bilan\n@islomuz_quron_bot")
    await mes.answer_photo("https://t.me/IT_info_chat/163", caption="Jizzax vaqti bilan\n@islomuz_quron_bot")
    await mes.answer_photo("https://t.me/IT_info_chat/164", caption="Samarqand vaqti bilan\n@islomuz_quron_bot")
    await mes.answer_photo("https://t.me/IT_info_chat/165", caption="Qarshi vaqti bilan\n@islomuz_quron_bot")
    await mes.answer_photo("https://t.me/IT_info_chat/166", caption="Termiz vaqti bilan\n@islomuz_quron_bot")
    await mes.answer_photo("https://t.me/IT_info_chat/167", caption="Buxoro vaqti bilan\n@islomuz_quron_bot")
    await mes.answer_photo("https://t.me/IT_info_chat/168", caption="Navoiy vaqti bilan\n@islomuz_quron_bot")
    await mes.answer_photo("https://t.me/IT_info_chat/169", caption="Xiva vaqti bilan\n@islomuz_quron_bot")
    await mes.answer_photo("https://t.me/IT_info_chat/170", caption="Nukus vaqti bilan\n@islomuz_quron_bot")


@dp.message_handler(text="Ro'za nima?")
async def rozanima(mes: Message):
    await mes.answer("""
<b>
RO‘ZA QANDAY IBODAT?
Shar’iy istilohda esa Ramazon oyida tong otganidan to quyosh botguncha niyat bilan ovqat yemaslik, ichimlik ichmaslik, jinsiy yaqinlik qilmaslik “ro‘za” deyiladi. Ro‘za tutish Islom dinining besh rukni, besh asosidan biridir, Qur’on va Sunnat bilan sobit bo‘lgan.

Ro‘za aqli raso, sog‘lig‘i yaxshi bo‘lgan har bir musulmon erkakka hamda hayz va nifosdan pok bo‘lgan musulmon ayolga farz qilingan. Hayz va nifos ko‘rgan ayollar ro‘za tutishmaydi, keyin qoldirgan kunlarining qazosini tutib berishadi. Yangi oyni ko‘rib, ro‘zaga niyat qilish Ramazon ro‘zasining asosiy shartlaridandir. Ramazon oyida noshar’iy amallar qilmaslik, tilni g‘iybat, yolg‘on so‘zlardan tiyish, o‘zgaga ozor bermaslik, yaxshi xulqli va rahm-shafqatli bo‘lish ro‘zaning odoblaridandir.

Ramazon kechasida turib saharlik qilishning o‘zi ro‘zaning niyatiga o‘tadi, chunki saharlik qilayotgan odamning ko‘ngliga ro‘za tutish niyati o‘z-o‘zidan keladi. Hanafiy mazhabida Ramazon tugagunicha har kuni niyat yangilab turiladi.

Hanafiy mazhabiga ko‘ra, Ramazon ro‘zasini tutishda har kungi niyatni quyosh oqqunigacha yangilab olsa ham bo‘laveradi, ya’ni kishi tongdan choshgohgacha ro‘zaga zid ish qilmay tursa, quyosh tikkaga kelishidan ozgina oldin o‘sha kunning ro‘zasi uchun niyat qilsa ham, ro‘za hisobiga o‘tadi. Lekin tongdan keyin yeb-ichib qo‘ygan bo‘lsa, keyin niyat qilsa durust bo‘lmaydi.

Ro‘zador kishiga yana ushbular sunnatdir: nafsni yomon niyatlardan to‘xtatish; foydasiz hamda uyatsiz so‘zlarni gapirishdan va eshitishdan o‘zini saqlash; birov bilan urishishdan, har qanday gunoh ishlardan o‘zni tortish; mumkin qadar istig‘for, zikr va tasbeh bilan band bo‘lish; Qur’on o‘qish; quyosh botgan vaqtda shom namozini o‘qishdan oldin bir qultum suv bilan bo‘lsa ham og‘iz ochish; Ramazon oyida har kuni xufton namozidan so‘ng yigirma rakat taroveh namozi o‘qish; taroveh namozida Qur’oni Karimni o‘qib yoki eshitib xatm qilish; Ramazonda xuftonni jamoat bilan o‘qigan kishining vitr namozini ham jamoat bilan o‘qishi.

Nafsni poklash va axloqni sayqallashda namoz va zakotdan keyin ro‘za ibodati keladi. Insonni yo‘ldan uradigan narsalar ichida qorin va jinsiy shahvatlar eng kuchlilaridan ekani hech kimga sir emas. Ro‘zaning foydalaridan biri xuddi o‘sha ikki shahvatni jilovlashga xizmat qilishidir.

Manba: https://islom.uz/ruza/1

@islomuz_quron_bot
</b>
""")


@dp.message_handler(text="Ro'zaning shartlari")
async def shartlari(mes: Message):
    await mes.answer("""
<b>
RO‘ZANING SHARTLARI
Ro‘za durust bo‘lishi uchun uch xil shart topilishi lozim.

Birinchi shart – zimmaga lozim bo‘lish shartlari.

Bu shartlar to‘rttadir:

1. Islom. Musulmon bo‘lmagan odamga ro‘za farz bo‘lmaydi. Unday odam ro‘za tutsa ham, ro‘zasi ibodat o‘rniga o‘tmaydi. Kofir odam Ramazonda Islomga kirsa, o‘sha kundan boshlab ro‘za tutadi.

2. Aql. Aqli yo‘q odamga ro‘za farz bo‘lmaydi, chunki u mukallaf emas.

3. Balog‘at. Balog‘atga yetmagan yosh bolalarga ro‘za farz bo‘lmaydi. Ramazon oyida balog‘atga yetganlar o‘sha kundan boshlab ro‘za tutishni boshlaydilar.

Ikkinchi shart – ro‘zani ado etish uchun lozim shartlar:

Bu shartlar ikkitadir:

1) Sog‘lom bo‘lish. Bemor kishiga ro‘za tutish vojib emas.

2) Muqim bo‘lish. Musofirga ro‘za tutish farz emas. U safardan qaytganda qazosini tutib beradi.

Uchinchi shart – ro‘zaning to‘g‘ri bo‘lishi shartlari.

Bu shartlar uchtadir:

1) Niyat. Niyatsiz ro‘za durust bo‘lmaydi.

2) Nifos va hayzdan xoli bo‘lish. Nifos va hayzli bo‘laturib tutilgan ro‘za durust bo‘lmaydi.

Ramazon ro‘zasining adosi va qazosi shar’iy kunduzning yarmidan avval niyat qilish bilan to‘g‘ri bo‘ladi.

Ma’lumki, qilinishi lozim bo‘lgan amalni shariatda belgilangan vaqtda qilish “ado” deyiladi. Qilinishi lozim bo‘lgan amalni belgilangan vaqtidan keyin bajarish “qazo” deyiladi.

Ramazon ro‘zasini vaqtida tutish farz. Agar u vaqtida ado qilinmagan bo‘lsa, qazosini tutish farz.

Shuningdek, kafforat ro‘zalari ham vojibdir. Birovni xato, ehtiyotsizlik sababli o‘ldirib qo‘ygan yoki ayolini zihor qilgan odam boshqa kafforatlarni bajara olmasa, ketma-ket ikki oy ro‘za tutishi vojib bo‘ladi.

Shar’iy kunduz tong otgandan (subhi sodiqdan) boshlanib, quyosh botguncha davom etadi. Shar’iy bo‘lmagan kunduz esa «lug‘aviy kunduz» deb ataladi va u quyosh chiqqandan boshlab botguncha davom etadi. Demak, ro‘za tutmoqchi bo‘lgan kishi tong otgandan boshlab kunduzning yarmigacha niyat qilib olsa, ro‘zasi to‘g‘ri bo‘ladi.

@islomuz_quron_bot
</b>    
""")


@dp.message_handler(text="Ro'zaning turlari")
async def turlari(ms: Message):
    await ms.answer("""
<b>
RO‘ZANING TURLARI
Ro‘zaning turlari to‘rttadir:

Lozim ro‘za.

Lozim ro‘za ikkiga: farz va vojibga bo‘linadi.

Farz ro‘za. U ham ikkiga: tayin qilingan va tayin qilinmagan farz ro‘zaga bo‘linadi.

Tayin qilingan farz ro‘za – Ramazon ro‘zasini ado etishdir. Bu Qur’on, sunnat va ulamolar ijmo’i bilan sobit bo‘lgan.

Tayin qilinmagan farz ro‘za – Ramazonning qazosi va kafforatining ro‘zasidir.

Shuningdek, hayz va nifosli ayollar, homilador va emizikli ayollar ham imkon topganlarida Ramazonning qazo ro‘zasini tutadilar.

Vojib ro‘za ham ikkiga: tayin qilingan va tayin qilinmagan vojib ro‘zaga bo‘linadi.

Tayin qilingan vojib ro‘za – muayyan nazr (tayinli kun) ro‘za va Ramazon oyining hilolini ko‘rib, shahodati qabul qilinmagan kishining ro‘zasidir.

Tayin qilinmagan vojib ro‘za:

a) Nazr ro‘za (mutlaq ro‘za ham deyiladi). Bu kunini tayin qilmasdan, bir kun ro‘za tutishni nazr qilgan kishining ro‘zasidir. Masalan, «Falon ishim amalga oshsa, bir kun ro‘za tutishni nazr qildim» deyilgani kabi.

b) Muayyan kunda ro‘za tutishni nazr qilib, tuta olmagan kishining qazo ro‘zasi.

v) Ro‘za tutishga qasam ichib, zimmasiga ro‘zani vojib qilib olgan kishining ro‘zasi.

g) Nafl ro‘zani tutishni boshlab, oxiriga yetkazmay, ochib yuborgan kishining o‘sha kun uchun tutadigan qazo ro‘zasi.

d) Kafforat ro‘zalari: zihor, qatl, Ramazonning ro‘zasini qasddan ochib yuborish va qasamni buzganligining kafforati uchun tutiladigan ro‘zalar.

ye) Tamattu’ va qiron uchun ehromga kirib, qurbonlik qila olmagan kishining o‘n kunlik ro‘zasi.

j) Ehromdalik chog‘ida, vaqti kirmasidan oldin soch oldirgan kishining kafforat uchun tutadigan uch kunlik ro‘zasi.

z) Haramda ov qilishning jazosi uchun tutiladigan ro‘za.

i) E’tikofini buzib qo‘ygan kishining qazo ro‘zasi.

@islomuz_quron_bot
</b>  
""")


@dp.message_handler(text="Ro'zaning niyati")
async def niyat(mes: Message):
    await mes.answer("""
<b>
RO‘ZANING NIYATI
“Niyat” so‘zi lug‘atda «qasd qilish» ma’nosini anglatadi. Shar’iy istilohda esa niyat deb qalbning bir ishni qilishga azmu qaror ila, ikkilanishsiz e’tiqod qilishiga aytiladi. Demak, kishi qalbida ertaga Ramazonning kunlaridan biri ekanini bilsa va ro‘za tutishni ko‘nglidan o‘tkazsa, niyat qilgan bo‘ladi.

Niyat masalasida ro‘zalar ikkiga bo‘linadi:

1. Kechasi niyat qilish va tayin qilish shart bo‘lgan ro‘zalar. Bunday ro‘zalar «zimmada sobit bo‘lgan ro‘zalar» ham deyiladi. Ular Ramazonning qazosi, buzib yuborilgan nafl ro‘zalarning qazosi, kafforat uchun tutiladigan ro‘zalar va mutlaq nazr qilingan ro‘zalardir.

2. Kechasi niyat qilish va tayin qilish shart bo‘lmagan ro‘zalar. Bunday ro‘zalar «muayyan zamonga bog‘liq ro‘zalar» ham deyiladi. Ular Ramazon ro‘zasi va barcha nafl ro‘zalar bo‘lib, shar’iy kunduzning yarmidan oldin qilingan niyat bilan to‘g‘ri bo‘laveradi.

Ramazon ro‘zasini nafl niyati bilan yoki mutlaq niyat yoxud boshqa vojib ro‘za niyati bilan ado qilsa ham bo‘ladi. Faqat safarda va bemorlikda bo‘lmaydi.

Ramazon ro‘zasi kabi nafl va muayyan nazr ro‘zani ham shar’iy kunduzning yarmidan avvalgi niyat bilan tutsa bo‘ladi. Faqat nafl va muayyan nazr ro‘zani boshqa vojib ro‘za niyati bilan tutib bo‘lmaydi, chunki ro‘za tutuvchi o‘ziga vojib bo‘lgan narsani o‘zi bekor qila olmaydi.

Qazo, kafforat va mutlaq nazr ro‘zalar uchun ularni kechasi tayin qilib, niyat qilish shart qilingan, chunki bunday ro‘zalar uchun muayyan vaqt tayin qilinmagan. Shuning uchun ularning boshlanish vaqtini tayin qilish vojib bo‘ladi.

Sha’bon oyining yigirma to‘qqizinchi kuni kechqurun quyosh botayotganda Ramazonning hiloli ko‘rinmasa va havo bulutli bo‘lsa, o‘ttizinchi kun shak kuni bo‘ladi, chunki o‘sha kun sha’bonning o‘ttizinchi kunimi yoki Ramazonning birinchi kunimi degan shak, ikkilanish bo‘ladi. Agar havo ochiq bo‘lsa ham oy ko‘rinmasa, shak bo‘lmaydi.

Niyat qilishning eng afzal vaqti iftor qilish paytida ertangi kunning ro‘zasini niyat qilishdir. Ramazon oyida ro‘za kunlari ekanini bilsa-da, ro‘za tutishni ham, tutmaslikni ham niyat qilmay tong ottirsa, ro‘zador bo‘lib qolmaydi. Zero, ro‘za kunlari ekanini bilishning o‘zi bilan ro‘zador bo‘lib qolinmaydi. «Inshaalloh, ertaga ro‘za tutaman» deyish bilan ham niyat durust bo‘laveradi, chunki ro‘zada bu kalimalar Alloh taolodan tavfiq, madad umidini ifoda qiladi.

Bir kishi har kuni ro‘za tutmoqchi bo‘lib saharlik qilsa, tili bilan ham, dili bilan ham ro‘zani niyat qilmasa ham, saharlik qilgani niyat o‘rniga o‘tadi. Lekin saharlik qilayotgan vaqtda ro‘za tutmaslikni niyat qilsa yoki odati har kuni o‘sha vaqtda taomlanish bo‘lsa yoxud hamma qatori saharlikka tursayu, o‘zi ro‘za tutmaydigan kishi bo‘lsa, uning saharlik qilgani niyat o‘rniga o‘tmaydi. Saharlik niyatning o‘rniga o‘tishi Ramazonning ro‘zasida, tayin qilingan nazrda va nafl ro‘zalardadir. Bundan boshqalarda esa saharlik qilish bilan birgalikda qaysi ro‘zani tutayotganini dil bilan niyat qilishi zarur. Kechaning avvalida «saharlikka turaman» deb niyat qilish ro‘za niyatining o‘rniga o‘tmaydi.

Quyosh botishi bilan ertangi kunning ro‘zasini niyat qilsa, niyati durust bo‘ladi. Masalan, bir kishi shunday niyat qilib, behush bo‘lib qolsayu, behushligi ertasi kunning quyoshi botgunicha davom etsa ham, u o‘sha kuni ro‘zador bo‘lgan hisoblanadi. Quyosh botishidan avval yoki botayotganda ertangi kunning ro‘zasini niyat qilishning o‘zi kifoya qilmaydi, balki quyosh botgandan so‘ng qayta niyat qilish zarur.

@islomuz_quron_bot
</b>    
""")


@dp.message_handler(text="Saharlik va iftorlik")
async def saharlik(mes: Message):
    await mes.answer(
"""
<b>
SAHARLIK VA IFTORLIK
Alloh taoloning har bir amri hikmatlarga boydir. «Allohning rahmati bahona qidirur» degan mashhur maqol bor. Alloh bu ummatga rahmatini yog‘dirishni iroda qilib, O‘z Payg‘ambari orqali saharlik va iftorlik qilishni sunnat qildi.

Musulmon kishi qorni to‘q bo‘lsa ham, taomga ehtiyoji bo‘lmasa ham saharlikda birorta xurmo yoki bir-ikki qultum suv ichib olsa, Payg‘ambarimiz alayhissalomning sunnatlariga ergashgan bo‘ladi. Zero, Anas ibn Molik roziyallohu anhu u zotning «Saharlik qilinglar, saharlikda baraka bor», deganlarini aytgan.

Tobe’inlardan Abu Atiyya va Masruqlar Oishaning huzuriga kirib, «Ey mo‘minlarning onasi, Muhammad sollallohu alayhi vasallamning sahobalaridan ikki kishi yaxshilikda musobaqalashishadi. Biri iftor bilan (shom) namozni tezlatadi. Boshqasi esa iftor bilan (shom) namozni ortga suradi», deyishdi. Oisha: «Qay biri iftorni va namozni tezlatadi?», deb so‘radi. «Abdulloh ibn Mas’ud», deyishdi. Oisha: «Rasululloh sollallohu alayhi vasallam shunday qilar edilar», dedilar. Iftor va namozni ortga surgan Abu Muso edi».

Abdulloh ibn Amr roziyallohu anhumodan rivoyat qilinadi:

«Rasululloh sollallohu alayhi vasallamning shunday deganlarini eshitdim: “Iftor paytida ro‘zadorning mustajob duosi bor”.

Sahl ibn Sa’d roziyallohu anhudan rivoyat qilinadi:

«Rasululloh sollallohu alayhi vasallam: «Modomiki iftorni tez qilishar ekan, kishilar yaxshilikda bo‘lurlar», dedilar».

Ro‘za tutish (saharlik, og‘iz yopish) duosi

نَوَيْتُ أَنْ أَصُومَ صَوْمَ شَهْرَ رَمَضَانَ مِنَ الْفَجْرِ إِلَى الْمَغْرِبِ، خَالِصًا لِلهِ تَعَالَى أَللهُ أَكْبَرُ

Navaytu an asuvma sovma shahri ramazona minal fajri ilal mag‘ribi, xolisan lillahi ta’aalaa Allohu akbar.

Ma’nosi: Ramazon oyining ro‘zasini subhdan to kun botguncha tutmoqni niyat qildim. Xolis Alloh uchun Alloh buyukdir.

Iftorlik (og‘iz ochish) duosi

اَللَّهُمَّ لَكَ صُمْتُ وَ بِكَ آمَنْتُ وَ عَلَيْكَ تَوَكَّلْتُ وَ عَلَى رِزْقِكَ أَفْتَرْتُ، فَغْفِرْلِى مَا قَدَّمْتُ وَ مَا أَخَّرْتُ بِرَحْمَتِكَ يَا أَرْحَمَ الرَّاحِمِينَ

Allohumma laka sumtu va bika aamantu va a’layka tavakkaltu va a’laa rizqika aftartu, fag‘firliy ma qoddamtu va maa axxortu birohmatika yaa arhamar roohimiyn.

Ma’nosi: Ey Alloh, ushbu Ro‘zamni Sen uchun tutdim va Senga iymon keltirdim va Senga tavakkal qildim va bergan rizqing bilan iftor qildim. Ey mehribonlarning eng mehriboni, mening avvalgi va keyingi gunohlarimni mag‘firat qilgil.

@islomuz_quron_bot
</b>
"""
    )


@dp.message_handler(text="Ro'zaning mustahablari")
async def mustahablar(mes: Message):
    await mes.answer("""
<b>
Quyidagi amallar ro‘zaning mustahablaridir:

1. Biror narsa bilan, bir qultum suv bilan bo‘lsa ham saharlik qilish, saharlikni kechaning oxirigacha surish.

2. Quyosh botishi bilan shom namozini o‘qishdan oldin darhol og‘izni ochish. Shirin va ho‘l narsa bilan og‘iz ochish afzal.

3. Og‘izni ochishda rivoyat qilingan lafzlar bilan duo qilish.

4. Ro‘zadorlarga iftor qilib berish.

5. Junublik, hayz va nifosdan qilinadigan g‘uslni kechga qo‘ymay, tong otishidan oldin qilib olish.

6. Til hamda a’zolarni ortiqcha gap-so‘z va amallardan tiyish.

7. Ro‘zani buzmaydigan, ammo huzurbaxsh narsalarni tark qilish.

8. Oila a’zolari va qarindoshlarga kengchilik qilish. Beva-bechora va kambag‘allarga xayr-ehsonni ko‘paytirish.

9. Qur’on qiroati, ilm suhbatlari, zikr va salavotlarni ko‘paytirish.

RO‘ZANING DARAJALARI
Ahli haqning nazdida ro‘zaning darajasi uchtadir:

Birinchi daraja ommaning ro‘zasi bo‘lib, u qorin va farjning istak-xohishlaridan tiyilishdir.

Ikkinchi daraja xoslarning ro‘zasi bo‘lib, u birinchi darajaga ziyoda o‘laroq ko‘z, quloq, tilni, oyoq, qo‘l va boshqa a’zolarni ham gunohlardan tiyishdir.

Uchinchi daraja xoslardan ham xoslarning ro‘zasi bo‘lib, u avvalgi ikki darajaga ziyoda o‘laroq qalbni behuda qiziqishlardan, dunyoviy fikrlardan va Alloh taolodan boshqa narsalardan tiyishdan iboratdir.

Xoslarning ro‘zasi «solihlar ro‘zasi» deb ham nomlanadi. Bu darajadagi ro‘zaning mukammal bo‘lishi quyidagi omillar bilan ro‘yobga chiqadi:

1. Barcha yoqimsiz va yomon narsalardan ko‘zni tiyish hamda qalbni Alloh taoloning zikridan to‘sadigan narsalarga mashg‘ul qilmaslik.

2. Tilni yolg‘on, g‘iybat, chaqimchilik, fahsh-uyat gaplar, jafo, xusumat, maqtanchoqlikka o‘xshash narsalardan tiyib, sukutni lozim tutish. Uni Alloh taoloning zikri va Qur’on tilovati bilan mashg‘ul qilish. Bu, tilning ro‘zasidir.

3. Quloqni eshitish makruh bo‘lgan barcha narsalardan, boshqacha qilib aytganda, yuqorida sanab o‘tilgan narsalarning hammasidan saqlash. Chunki gapirish mumkin bo‘lmagan barcha narsani eshitish ham mumkin emas.

4. Qo‘l, oyoq va boshqa a’zolarni gunohlardan saqlash hamda iftordan keyin qorinni shubhali taomlardan saqlash. Zotan, qorinni halol narsadan saqlab ro‘za tutib, keyin halol bo‘lmagan narsa bilan iftor qilishning ma’nosi ham yo‘q. Harom narsalar dinni halok qiluvchi zahardir. Halol esa dori kabi ozi foydali, ko‘pi zararlidir.

5. Iftorda haddan tashqari ko‘p yeb, qorinni to‘ydirib yuborishdan saqlanish. Bunday qilish bilan ro‘zadan ko‘zlangan maqsad amalga oshmaydi. Chunki ro‘zadan ko‘zlangan maqsadlardan biri ochlikning mashaqqatini his qilishdir. Mazkur maqsadga erishish esa, ro‘zadan boshqa vaqtlarda nonushtada tanovul qiladigan taomni saharlikda va kechki ovqatda tanovul qiladiganini iftorda iste’mol qilish bilan bo‘ladi.

Iftordan so‘ng qalb xavf va rajo orasida bo‘lishi lozim, chunki ro‘zasi qabul bo‘lib, muqarrab bandalar qatoriga qo‘shildimi yoki qabul bo‘lmay, g‘azabga uchraganlardan bo‘ldimi, aniq emas. Har bir ibodatdan forig‘ bo‘lgandan so‘ng shu holatda bo‘lish lozim.

Ramazon taqvo oyidir. Bu oyda xulqimiz yanada yuksalib, harom va shubhalardan har qachongidan ham ko‘proq tiyilishimiz zarur. Shunday tabarruk oyda qiz-kelinlarimizni milliyligimizga yot bo‘lgan holatda kiyinib yurishdan, erkaklarimizni nomahramlarga ko‘z tikishdan qaytarishimiz lozim. Vaholanki, hadisda «Ko‘ngilning taqvosi haromga qaramaslikdir», deyilgan.

Ramazon ibodatlarni ko‘paytirish, gunohlarga mag‘firat so‘rash, Qur’on bilan oshno bo‘lish, Allohga bandalikni yuksak darajaga ko‘tarish oyidir. Shunday bo‘lgach, Ramazonni taqvo, halollik, husni xulq va yaxshiliklar oyiga aylantirish har bir musulmonning burchidir.

@islomuz_quron_bot
</b>    
""")



@dp.message_handler(text="Ro'zaning buzilish xollari")
async def buzilish(mes: Message):
    await mes.answer("""
<b>
RO‘ZANI BUZADIGAN NARSALAR
Ro‘zaning buzilishi ikki xil bo‘ladi.

Birinchisi – qazo va kafforatni vojib qiladigan holatlar.

Ikkinchisi – faqat qazoni vojib qiladigan holatlar.

Qazo va kafforat vojib bo‘ladigan holatlar. Kafforat Ramazonning hurmatini oyoqosti qilingani uchun vojib bo‘ladi. Ramazonning farz ro‘zasini ado qilishni niyat qilib ro‘za tutgan odam uni o‘z ixtiyori bilan, majburlashsiz va shar’iy uzrsiz qasddan ochib yuborsa, ham qazosini tutadi, ham kafforatni ado etadi. Lekin Ramazonning qazosini yoki boshqa ro‘zalarni qasddan buzsa kafforat vojib bo‘lmaydi.

Kafforat quyidagi holatlarda vojib bo‘ladi:

1. G‘izo yoki shu kabi narsani shar’iy uzrsiz yeyish. Odatda ozuqa sifatida tanovul qilinadigan barcha narsalar g‘izoga kiradi. Dori, papiros, sigara, afyun, nasha va shunga o‘xshash narsalar ham g‘izo toifasiga kiradi. Ushbu holatlarda ro‘zasini ochgan odam ham qazosini tutadi, ham qul ozod qilish yoki oltmish kun ketma-ket ro‘za tutish, unga qodir bo‘lmasa, oltmish miskinga taom berish bilan kafforatni ado qiladi.

2. Birovni g‘iybat qilgani, qon oldirgani, shahvat bilan ushlagani yoki o‘pgani, quchoqlashib yotgani, mo‘ylabini moylagani sababli «ro‘zam ochilib ketdi» deb o‘y lab, qasddan yeb-ichib yuborgan odam ham qazo tutadi, ham kafforatni ado qiladi (Lekin faqih kishi «ro‘zang ochilibdi» deb fatvo bersa, bundan mustasno. Unda faqat qazo tutadi, kafforat vojib bo‘lmaydi).

3. Og‘ziga kirgan yomg‘ir suvini, xotinining tupugini lazzat uchun ichiga yutsa, kesakxo‘r odam kesakni yutib yuborsa, ham qazo tutib, ham kafforat ado qiladi.

4. Farj shahvatini to‘la ravishda qondirish. Bunda maniy to‘kilmasa ham qazo va kafforat vojib bo‘ladi. Jumhur ulamolar: «Jimo’da qatnashgani uchun ayol kishi ham kafforat beradi», deyishgan.

5. Ayol kishi yosh bolaning yoki majnunning o‘ziga yaqinlik qilishiga imkon bersa, unga ham qazo, ham kafforat vojib bo‘ladi.

Batafsil: https://islom.uz/ruza/1#block10
@islomuz_quron_bot  
</b>
""")


@dp.message_handler(text="Tutish makruh bo'lgan kunlar")
async def mmakruhk(ms: Message):
    await ms.answer("""
<b>
RO‘ZA TUTISH HAROM BO‘LGAN KUNLAR
Ro‘za tutish harom bo‘lgan kunlar quyidagilardir:

1. Iydul-fitr kuni, Iydul-azho kuni va undan keyingi uch kun. Bu kunlarda ro‘za tutish haromdir, chunki bu kunlar xursandchilik kunlaridir.

2. Shak kuni, ya’ni Ramazon kirishidan oldingi kunda ro‘za tutish.

3. Ro‘za tutsa halok bo‘lishini bila turib ro‘za tutgan odamning ro‘zasi.

4. Ayollarning hayz va nifos ko‘rgan kunlari. Bu kunlarda ro‘za tutish mumkin emas.

RO‘ZA TUTISH MAKRUH BO‘LGAN KUNLAR
Quyidagi kunlarda ro‘za tutish makruhdir:

1. Ayol kishining erining iznisiz yoki roziligini bilmay turib nafl ro‘za tutishi (agar er yaqinlikka ojizlik qiladigan darajada bemor bo‘lsa, yoki ro‘zador bo‘lsa, yoxud haj yo umraga ehrom bog‘lagan bo‘lsa, makruh emas).

2. Ashuro kunining yolg‘iz o‘zida ro‘za tutish.

3. Juma kunini xoslab ro‘za tutish.

4. Shanba kunini ulug‘lab ro‘za tutish.

5. Yakshanba kunini ulug‘lab ro‘za tutish.

6. Navro‘z kuni ro‘za tutish.

7. Mehrjon kuni ro‘za tutish.

8. Uzluksiz har kuni ro‘za tutish.

9. Gapirmasdan ro‘za tutish.

10. Ulab (saharlik qilmay) ro‘za tutish.

11. Musofirning qiynalib ro‘za tutishi.

@islomuz_quron_bot
</b>    
""")
# KeyboardButton(text="Tutish makruh bo'lgan kunlar")