from loader import dp

from aiogram.types import Message
from keyboards.default.namoz_keyboard import namoz, turli_namozlar, namoz_video


@dp.message_handler(text="🕌 Namoz")
async def namoz_vaqti(mes: Message):
    await mes.answer("Namoz bo'limi:", reply_markup=namoz)


@dp.message_handler(text="Namoz nima?")
async def namoznima(mes: Message):
    text = """
<b>
Namoz haqida oyat va hadislar

Namoz Islomning asosiy shartlaridan biri hisoblanadi. Alloh taolo bandalariga farz qilib qo‘ygan. Namoz Alloh bergan hadsiz-hisobsiz ne’matlarga bandasining shukronasi hamdir. Namoz ibodati tufayli kishining Alloh nazdidagi darajasi yuksaladi. Namozxon oxirat hayotiga tayyorgarlik ko‘rib boradi. Turli bahonalar bilan namoz o‘qimay yurgan kishi Allohning buyrug‘iga qarshi chiqqan bo‘ladi. Bu esa, katta musibatdir.

Qur’oni karimda namoz o‘qish amr etilgan ko‘plab oyatlar bor (mazmunlari):

«Namozni mukammal ado etingiz, zakot beringiz va ruku qiluvchilar bilan birga ruku qilingiz» (Baqara, 43).

«Namozni mukammal ado etingiz va zakot beringiz!» (Baqara, 110).

«Alloh imonlaringizni (Baytul-Maqdisga qarab o‘qigan namozlaringiz ajrini) zoe ketkizmas. Albatta, Alloh odamlarga mehribon va rahmlidir» (Baqara, 143).

«(Ey Muhammad), imon keltirgan bandalarimga ayting, namozni mukammal ado etsinlar hamda savdo-sotiq va oshna-og‘aynigarchilik bo‘lmaydigan Kun (qiyomat) kelmay turib, Biz ularga rizq qilib bergan narsalardan xufyona va oshkora ehson qilsinlar!» (Ibrohim, 31).

"Quyosh og‘ishidan to tun qorong‘usigacha namozni mukammal ado qiling va tonggi o‘qishni (bomdod namozini) ham (ado qiling). Zero, tonggi o‘qish (farishtalar) hozir bo‘ladigan (namoz)dir. Tunda (bir qismida) uyg‘onib o‘zingiz uchun tahajjud (nafl) namozini o‘qing! Shoyadki, Rabbingiz Sizni (Qiyomat kunida) maqtovli (shafoat qiladigan maqomda) tiriltirsa» (Al-Isro, 7879).

«Ahlingizni namoz (o‘qish)ga buyuring va (o‘zingiz ham) unga (namozga) bardoshli bo‘ling!» (Toha, 132).

«Darhaqiqat, mo‘minlar najot topdilar. Ular namozlarga (qo‘rquv va umid bilan) bo‘yin eguvchi kishilardirlar. Ular (barcha) namozlarni (vaqtida ado etib qazo bo‘lishdan) saqlaguvchi kishilardir» (Mo‘minlar, 12, 9).

«Albatta, namoz fahsh va yomonlikdan qaytarur! Albatta, Allohning zikri (barcha narsadan) ulug‘dir!» (Ankabut, 45).

«Bas (ey, Muhammad), ular (kofirlar) aytayotgan so‘zlarga sabr qiling va Quyosh chiqishidan va botishidan avval Rabbingizga hamd bilan tasbeh ayting (namoz o‘qing)! Yana kechaning (bir qismida) va sajdalar (namozlar) ortidan tasbeh ayting!» (Qof, 3940).

«(Ey Muhammad,) Siz Rabbingizning hukmiga sabr qiling! Zotan, Siz Bizning ko‘z o‘ngimizda (himoyamizda)dirsiz! (Tongdan uyqudan) turgan paytingizda, Rabbingizga hamd bilan tasbeh ayting! Shuningdek, kechadan (vaqt ajratib) va yulduzlar yuz o‘girgach (botgach saharda) ham Unga tasbeh ayting» (Tur, 48-49).

«Darhaqiqat, inson betoqat qilib yaratilgandir. Qachonki unga yomonlik (kambag‘allik yoki musibat) yetsa, u o‘ta besabrlik qiluvchidir. Qachonki unga yaxshilik (boylik, salomatlik) yetsa, u o‘ta man etuvchi (baxil)dir. Faqat namozxonlar bundan mustasnodirlar» (Maorij, 1923). 

@islomuz_quron_bot
</b>
"""
    text2 = """
<b>
HADISLARDAN NAMUNALAR 

* Payg‘ambarimiz (s.a.v.) ashoblaridan so‘radilar: «Birortangiz uyingizning oldidan oqib o‘tadigan daryoda (yoki soyda) har kuni besh mahal yuvinsangiz, badanimda kir qolibdi, deb aytasizmi?» Sahobalar: «Sira ham kir qolmaydi», deyishdi. Rasuli Akram: «Besh vaqt namoz ham shunga o‘xshash bo‘lib, Alloh taolo bu o‘qilgan namozlar tufayli gunohlarni kechiradi».

* «Asr namozini qazo qilib qo‘ygan odam bola-chaqasiyu mol-dunyosidan ajragan kishi yanglig‘dir».

* «Qorong‘u kechalarda masjidga borgan kishilarga, Qiyomat kuni bir nurga mazhar bo‘lishlari xushxabarini yetkazing».

* «Sizlardan birlaringiz namoz o‘qigan joyda tahoratini buzmasdan o‘tirgan muddatgacha, farishtalar: «Iloho, bu kishining gunohlarini kechir va unga rahm ayla», deb duo etishadi»

* «Allohga qasamki, shunday narsa xayolimdan o‘tyapti: o‘tin to‘plashni buyursam va o‘tinlar to‘plansa. Keyin namozga buyursam, namoz uchun azon aytilsa, keyin bir kishini mo‘minlarga imomlikka o‘tishni buyursam-da, namozga kelmaganlarning borib uylarini yoqsam...»

* «Mo‘minlar xufton va bomdod namozlaridagi savobni bilganlarida edi, bu namozlarni jamoat bilan o‘qish uchun, emaklab bo‘lsa ham, masjidga kelishar edi».

* «Namoz inson bilan shirk va kufr o‘rtasidagi bir pardadir. Namozni tark etish bu pardani ko‘tarish bo‘ladi».

* «Ular (kofirlar) bilan bizning o‘rtamizni farqlaydigan alomat namozdir. Binobarin, namozni tark qilgan kimsa kofirlarga o‘xshabdi».

* «Banda Qiyomat kunida eng avvalo namozdan hisob-kitob qilinadi. Agar namozi durust chiqsa, qutulibdi va yutibdi. Agar namozi durust chiqmasa, yutqazibdi. Farz namozlari kam chiqsa, Alloh azza va jalla: «Qarang-chi, qulimning nafl namozlari bormi?» deydi. Namozlarining kami nafl namozlar bilan to‘ldiriladi. Qolgan amallari ham shu tarzda hisob-kitob qilinadi».

* «Bir kuni Payg‘ambar, alayhissalom, huzurlarida namoz o‘qimay tong otguncha uxlagan bir kishining nomi tilga olindi. Rasuli Akram: «Unday bo‘lsa, u odamning quloqlariga yo qulog‘iga shayton bavl etibdi», deya marhamat qildilar».

* «Sizlardan birov uxlab qolsa, shayton uning orqa miyasiga uch tugun tugib qo‘yadi va har tugunga: «Hali tunlar uzun, (bemalol) uxla», deya afsun o‘qiydi. Agar u odam uy-g‘onib Allohni zikr etsa, tugunlardan bittasi, tahorat olganida yana biri, namoz o‘qiganida esa, qolgani ham yechiladi va qalbi quvonch va xushnudlikka to‘lib tong ottiradi. Aks holda, shayton tugib qo‘ygan tugunlarning ta’sirida dangasalik bilan tong otguncha uxlab qoladi».

* Kechasi turib ibodat qilgan va xotinini uyg‘otgan, xotini turishni xohlamasa, yuziga suv sepgan odamga Alloh rahmatini yog‘dirsin. Kechasi turib namoz o‘qigan va erini uyg‘otgan, eri turishni xohlamasa, yuziga suv sepgan xotinga Alloh rahmatini yog‘dirsin».

* «Namoz jannatning kalitidir».

* «Namoz dinning ustunidir».

* «Namoz mo‘minning me’rojidir».

* «Ey Muhammad, bir kecha-kunduzda ummatlaringga besh vaqt namozni farz qildim. O‘zimcha ahd qildimki, kim shu besh vaqt namozni o‘z vaqtida ado etib yursa, u kishini jannatga kiritaman. Kim o‘z vaqtida ado etib yurmasa, u banda xususida ahdim yo‘qdir» (Hadisi qudsiy).

@islomuz_quron_bot
</b>
"""
    await mes.answer(text)
    await mes.answer(text2)


@dp.message_handler(text="Poklanish")
async def poklanish(mes: Message):
    await mes.answer("""
<b>
NAMOZGA POKLANISH
 Bizning Islom dinimiz poklikka juda katta ahamiyat bergan va musulmonlarni namoz o‘qishdan avval tahorat (buning iloji bo‘lmaganda tayammum) qilishga buyurgan. Ular tahorat qilishayotganda yuzlari, qo‘llari va oyoqlarini yuvishadi. Shuningdek, Islom mo‘minlarni g‘usl qilish, bundan tashqari mo‘ylov va tirnoqlarini qisqartirish, kiyimlarini pokiza tutish, jamoat joylarida, xususan, juma va hayit namozlarida xushbo‘ylanib yurishga targ‘ib qiladi. 

 Darhaqiqat, Rasululloh sollallohu alayhi vasallam safardan qaytayotgan sahobalariga: «Sizlar birodarlaringiz huzuriga qaytmoqdasiz. Shunday ekan, ulovlaringizu liboslaringizni chiroyli holda tutinglar. Hatto odamlar ichida go‘yoki xol kabi ajrab turinglar. Albatta, Alloh buzuqlik va axloqsizlikni yaxshi ko‘rmaydi», deb aytganlar (Imom Abu Dovud rivoyat qilgan).

G'usl haqida: https://telegra.ph/Gusl-03-24
G'usl haqida: https://youtu.be/ZVx_fBoR_1U
Qachon g'usl qilamiz: https://youtu.be/h7ZpF_nHy0Q

Tahorat haqida: https://telegra.ph/Tahorat-03-24
Tahoratni o'rganamiz
Muhammad Sayyid: https://youtu.be/fFEPEbtpX7w
Ikrom Sharif: https://youtu.be/DGeyIaJ1308
Rustamjon domla: https://youtu.be/nM_bv2lu478
Tahoratdagi xatolar: https://youtu.be/eioXxMkxBOk

Tayammum haqida: https://telegra.ph/Tayammum-03-24
Tayammumni o'rganamiz: https://youtu.be/CoDPQYfkAeU

Manba: islom.uz
@islomuz_quron_bot
</b>""")


@dp.message_handler(text="Namoz va taxorat kitobi")
async def namozkitobi(mes: Message):
    await mes.answer_video("https://t.me/islomiy_mediya/11", caption="""
<b>
Android tizimi uchun
IOS tizimi uchun link:https://apps.apple.com/us/app/намоз/id1475091724

Shayx Muhammad Sodiq Muhammad Yusuf rahimahullohning kitoblari asosida tuzilgan ushbu dasturda tahorat qilish va namoz oʻqishni oʻrganish uchun eng zarur qoidalar keltirilgan boʻlib, yangi namozxonlar, yoshlar oʻrganishi uchun qulaydir.

@islomuz_quron_bot
@islomiy_mediya
</b>""")


@dp.message_handler(text="Namoz vaqtlari")
async def namozvaqti(mes: Message):
    await mes.answer(
        """
        <b>
        NAMOZ VAQTLARI
        Namozni oʻz vaqtida oʻqish farz valozimdir. Vaqti kirmasdan oʻqilgan namozlar hisobga oʻtmaydi. Vaqtida oʻqishga ulgurilmagan namozlarning qazosi oʻqiladi. 
        
        Aliy roziyallohu anhudan rivoyat qilinadi: 
        
        “Nabiy sollallohu alayhi vasallam u kishiga: «Ey Aliy, uch narsani ortga surmagin. Namozni vaqti kirganda, janozani hozir boʻlganda va ersiz ayol tengini topganda”, dedilar» 
        
        Imom Termiziy rivoyat qilgan. 
        
        Ibn Umar roziyallohu anhudan rivoyat qilinadi: 
        
        “Nabiy sollallohu alayhi vasallam: «Namozning avvalgi vaqti Allohning roziligidir. Oxirgi vaqti Allohning afvidir”, dedilar» 
        
        Imom Termiziy rivoyat qilgan. 
        
        Alloh taolo farz qilgan namozlarning oʻqish vaqti quyidagi paytlarda boʻladi: 
        
        1. Bomdod namozining vaqti – subhi sodiqdan (chin tong otgandan) kun chiqqunchadir. 
        
        2. Peshin namozining vaqti – quyosh zavolga (ogʻishga) ketganidan soʻng to narsalarning soyasi quyosh tikkaga kelgan paytdagi soyasidan tashqari oʻz uzunligiga nisbatan ikki baravar ortguniga qadar. 
        
        3. Asr namozining vaqti – har bir narsaning soyasi quyosh tikkaga kelgan paytdagi soyasidan tashqari oʻziga nisbatan ikki baravar ortganidan boshlab quyosh botgunchadir. 
        
        4. Shom namozining vaqti – kun botgan paytdan boshlab kunbotar tomonda shafaq (qizgʻish nurlar) gʻoyib boʻlgunchadir. 
        
        5. Xufton namozining vaqti – shafaq batamom yoʻqolgandan keyin kiradi. 
        
        Vitr namozi vaqti esa xufton oʻqilgandan keyingina kiradi. Xufton va vitr namozlarini subhi sodiqqacha oʻqisa boʻladi. 
        
        Bomdod namozini tong yorishganda oʻqish mustahab, aʼloroqdir. Soat boʻyicha hisoblansa, bomdodni kun chiqishidan 40 daqiqacha ilgari oʻqish mustahab vaqtiga muvofiq boʻladi. 
        
        Peshin namozini yoz faslida biroz kechiktirib, qish faslida esa vaqti kirishi bilan oʻqish mustahabdir. 
        
        Asr namozini quyosh tigʻini oʻzgartirmay, nursiz holatga kirishidan oldinroq oʻqish mustahabdir. 
        
        Shom namozini doimo quyosh botishi bilan oʻqish mustahabdir. 
        
        Xufton namozini kechaning uchdan birining oxirida oʻqish afzal va nihoyatda aʼlo boʻladi. Vitr namozini esa tun oxirida uygʻonishga qodir boʻlgan kishilar subh oldidan oʻqisalar, mustahab amal qilgan boʻlishadi. 
        
        Havo bulutli kunlarda asr va xufton namozlarini avvalgi vaqtlarida oʻqish hamda bomdod, peshin, shom namozlarini esa (vaqti kirgani maʼlum boʻlmasa) biroz kechiktirib oʻqish maqsadga muvofiqdir. 
        
        Quyidagi vaqtlarda namoz oʻqish, tilovat sajdasi qilish, janoza namozi oʻqish joiz emas (mumkin emas): 
        
        – kun chiqayotgan paytda;
        
        – kun qiyom (tikka)ga kelganida;
        
        – kun botish chogʻida;
        
        Bu paytlarda namoz oʻqish, Qurʼoni Karimdan sajda oyati oʻqilganda sajda qilish, janoza namozini shu vaqtga toʻgʻrilab oʻqish mumkin emas. Ammo shu kungi asr namozi kun botayotgan boʻlsa ham ado etilaveradi. 
        
        Ibn Abbos roziyallohu anhudan rivoyat qilinadi:
        
        “Menga eng rozi boʻlingan kishilar guvohlik berdilar. Ularning ichida eng rozi boʻlingani Umardir. «Albatta, Nabiy sollallohu alayhi vasallam bomdod namozidan keyin to quyosh chiqquncha va asrdan keyin (quyosh) botguncha namoz oʻqishdan qaytarganlar”, dedi»
        
        Imom Buxoriy, Muslim, Abu Dovud, Termiziy va Nasoiy rivoyat qilishgan. 
        
          Nafl (ixtiyoriy) namozlarni imom xutba oʻqish uchun minbarga chiqqanida, subhi sodiqdan kun chiqqunicha, asrni oʻqigan kishi shom namozini oʻqiguncha ado etishi makruhdir, yaʼni joiz emas.
        Manba: Islom.uz
        
        @islomuz_quron_bot
        </b>
        """
    )

    await mes.answer("""
<b>
Namoz vaqtlari, eng yaqin masjid va boshqa ma'lumotlarni quyidagi bot, kanal yoki saytlardan olishingiz mumkin:
@islomuz_namoz_bot
@islom_namoz_bot
@praytimeuz
praytime.uz
namozvaqti.uz

Dunyo shaharlari uchun namoz vaqtlari:
www.namazvakti.com
</b>
""")


@dp.message_handler(text="Namozni o'rganamiz")
async def namozniorganamiz(mes: Message):
    await mes.answer("""
NAMOZNING TURLARI
Farz namozlari – Alloh taoloning amri bilan har bir musulmon zimmasida burch hisoblangan besh vaqt namoz (bomdod, peshin, asr, shom, xufton) va juma namozi hamda (musulmonlardan ba’zilarining o‘qishi bilan boshqalardan soqit bo‘luvchi) janoza namozi. 

Vojib namozlar – har kuni xuftondan so‘ng o‘qiladigan vitr namozi, ramazon va qurbon hayiti namozlari, Baytullohdagi tavof namozi. 

Sunnat va nafl namozlari – besh vaqt farz namozlardan oldin yoki keyin o‘qiladigan sunnat namozlar, taroveh, istisqo, «Tahiyatul-masjid» namozi, zuho (choshgoh), tahajjud, istixora, hojat so‘rash namozlari, tahorat yoki g‘usldan so‘ng, safarga chiqayotganda, oy yoki quyosh tutilganda o‘qiladigan namozlar.""",
                     reply_markup=namoz_video)


@dp.message_handler(text="Erkaklar")
async def erkaklaruchunnamoz(mes: Message):
    await mes.answer_video("https://t.me/islomiy_mediya/27", caption="<b>Bomdod namozi\n@islomuz_quron_bot</b>")
    await mes.answer_video("https://t.me/islomiy_mediya/28", caption="<b>Peshin namozi\n@islomuz_quron_bot</b>")
    await mes.answer_video("https://t.me/islomiy_mediya/29", caption="<b>Asr namozi\n@islomuz_quron_bot</b>")
    await mes.answer_video("https://t.me/islomiy_mediya/30", caption="<b>Shom namozi\n@islomuz_quron_bot</b>")
    await mes.answer_video("https://t.me/islomiy_mediya/31", caption="<b>Xufton namozi\n@islomuz_quron_bot</b>")


@dp.message_handler(text="Ayollar")
async def ayollarnamoz(mes: Message):
    await mes.answer_video("https://t.me/islomiy_mediya/32", caption="<b>Bomdod namozi\n@islomuz_quron_bot</b>")
    await mes.answer_video("https://t.me/islomiy_mediya/33", caption="<b>Peshin namozi\n@islomuz_quron_bot</b>")
    await mes.answer_video("https://t.me/islomiy_mediya/34", caption="<b>Asr namozi\n@islomuz_quron_bot</b>")
    await mes.answer_video("https://t.me/islomiy_mediya/35", caption="<b>Shom namozi\n@islomuz_quron_bot</b>")
    await mes.answer_video("https://t.me/islomiy_mediya/36", caption="<b>Xufton namozi\n@islomuz_quron_bot</b>")


@dp.message_handler(text="Turli namozlar")
async def turlinamozlar(mes: Message):
    await mes.answer("Turli namozlar: ", reply_markup=turli_namozlar)


@dp.message_handler(text="Vitr namozi")
async def vitr(mes: Message):
    await mes.answer("""
<b>
VITR NAMOZI
Vitr namozi uch rakat boʻlib, bir salom bilan oʻqiladi. Vitr namozining avvalgi ikki rakati boshqa ikki rakatli namozlar kabi ado etiladi. Uchinchi rakatning rukuʼsidan oldin takbir aytib, qoʻllar quloqlar toʻgʻrisigacha koʻtariladi, yana kindik ostiga qoʻyiladi va shu holatda Qunut duosi oʻqiladi. Vitr namozining har bir rakatida Fotiha surasidan soʻng biror sura qoʻshib oʻqiladi. 

Imom Aʼzam mazhabidagi namozxon shofeʼiy mazhabidagi kishiga iqtido qilgan paytida imomning rukuʼdan keyin oʻqigan Qunut duosiga tobe boʻladi. Lekin bomdod namozida shofeʼiy mazhabidagi imom Qunut duosini oʻqiydigan boʻlsa, bu imomga iqtido qilgan hanafiy mazhabidagi namozxon sukut qilib, oʻqimay turadi. Ramazon oyida umraga borgan hanafiy mazhabidagilar vitrni oʻqishda Masjidul Haromning imomiga iqtido qilaveradilar.

Batafsil: https://telegra.ph/Vitr-namozi-03-25
Manba: islom.uz

@islomuz_quron_bot
</b>
""")


@dp.message_handler(text="Juma namozi")
async def jumanamoz(mes: Message):
    await mes.answer("""
<b>
JUMA NAMOZI
“Juma” soʻzi “jam boʻlish, toʻplanish” degan maʼnoni anglatadi. Alloh taolo moʻminlarga juma namozini farz etgan, buyurgan: “Ey iymon keltirganlar! Juma kunidagi namozga chorlangan paytda Allohning zikriga shoshiling va savdoni qoʻying!” (Juma surasi, 9-oyat). Shu kuni jamoat boʻlib ado etiladigan namoz esa “juma namozi” deyiladi. Alloh taolo osmonlaru yerni juma kuni yaratgan, Odam atoni shu kuni xalq etgan, uni shu kunda jannatga kiritib, u yerdan chiqargan. Qiyomat ham juma kuni keladi. Bu kunda duolar qabul boʻladigan alohida soat bor, moʻminning Alloh taolodan xayriyatni soʻrab qiladigan iltijosi shu vaqtga toʻgʻri kelib qolsa, Alloh uni albatta ijobat qiladi. Juma namozi miskin-faqirlarning hajiga tenglashtiriladi. Imom minbarga oʻtirgan vaqtda ikkinchi azon aytiladi va qavm imomga roʻpara boʻlgan holda xutbani tinglaydi. Imom tahorat bilan tik turib ikki marta xutba oʻqiydi va ular oʻrtasida bir muddat oʻtirishi lozim boʻladi. U xutbani tugatgach, takbir aytiladi va imom qavm bilan ikki rakat juma namozini oʻqiydi.

Juma namozi ikki rakat farz bo'lib, undan oldin va keyin to'rt rakat sunnat o'qiladi. Ilk va oxirgi sunnatlar peshin namozining sunnatlari kabi o'qiladi. Imomga iqtido qilib o'qiladigan ikki rakat farz esa, bomdod namozining farzi kabi o'qiladi.
Juma namozida ikki rakat farz o'qilmasdan oldin imom minbarda xutba qiladi.
Juma namozi hur, ozod, muqim, salomatligi joyida, oyoqlari sog' kishiga farzdir.
Juma namozining shartlari:
1) peshin namozi o'qiladigan vaqtda o'qish;
2) namozdan oldin xutba o'qish;
3) juma o'qiladigan joy hammaga ochiq bo'lishi;
4) imomdan tashqari kamida uch kishidan iborat jamoat bo'lishi;
5) imom juma namozini o'qishi uchun rasman ruxsatli bo'lishi;
6) juma o'qiladigan joy shahar yoxud shahar hukmida bo'lishi kerak.

        

Batafsil: https://telegra.ph/Juma-namozi-03-25
Manbalar: https://islom.uz/maqola/186
islom.ziyouz.com

@islomuz_quron_bot
</b>""")


@dp.message_handler(text="Janoza namozi")
async def janozanamoz(mes: Message):
    await mes.answer("""
<b>
Janoza namozi toʻrt takbirdan iborat boʻlib, uni oʻqish quyidagi tartibda amalga oshiriladi:

Janoza namozini oʻqishga niyat qilinadi.
 

Jamoat imomi “Allohu akbar” deb takbir aytgach, boshqalar ham ichida “Allohu akbar” deb aytib qoʻlni quloqlarning yumshoq yerigacha koʻtaradi va qoʻllarini bogʻlaydi.
 

Qoʻllar qovushtirilgach “Sano” duosi oʻqiladi:
“Subhanakallohumma va bihamdika va tabarokasmuka va taʼala jadduka va la ilaha gʻoyruk”.

 

Sano duosidan soʻng imom ikkinchi takbirni aytadi. Bunda qoʻllar koʻtarilmaydi va tananing boshqa aʼzolari ham oʻz holida turadi.
Eslatma! Baʼzi bir kishilarning takbir vaqtida, yaʼni imom “Allohu akbar” deb aytganda osmonga qarash holati koʻzatiladi. Bunday qilish nojoizdir.

 

Ikkinchi takbirni aytgach, quyidagi salavot aytiladi: “Allohumma solli ʼala Muhammad va ʼalaa aali Muhammad, kamaa sollayta ʼala Ibrohiyma va ʼalaa aali Ibrohiym, innaka hamiydum majiyd.
Allohumma baarik ʼalaa Muhammad va ʼalaa aali Muhammad, kamaa baarokta ʼalaa Ibrohiyma va ʼalaa aali Ibrohiym, innaka hamiydum majiyd”.

 

Salavotdan keyin uchinchi takbir aytiladi. Uchinchi takbirdan keyin mayyit haqqiga quyidagi duo oʻqiladi:
“Allohumma magʻfir lihayyinaa va mayyitinaa va shaahidinaa va gʻoibinaa va sogʻiyrinaa va kabiyrinaa va zakarinaa va unsaanaa. Allohumma man ahyayta huva minnaa fa ahyihi ʼalal Islaam va man tavaffayta huva minnaa fatavaffahu ʼalal iymaan”.

Maʼnosi: Allohim, bizning tiriklarimiz va mayyitlarimiz, hozirlarimiz va gʻoiblarimiz, kichiklarimiz va kattalarimiz, erkaklarimiz va ayollarimizni magʻfirat qilgin!

Allohim, Sen bizlardan kimni yashatadigan boʻlsang, uni Islomda yashatgin. Bizlardan kimni vafot ettirsang, uni imonda vafot ettir.

 

Mayyit haqqiga duo qilingach toʻrtinchi takbir aytiladi Toʻrtinchi takbirdan keyin duo qilinmasdan, ikki yonga salom beriladi.
Balogʻatga yetmagan bolalarga yoki majnunlarga janoza namozi oʻqilganda ularning gunohlari kechirilishi soʻralmaydi. Sababi ular gunohsizdirlar. Ularga quyidagi duo oʻqiladi:

“Allohumma, aʼizhu min ʼazaabil qobr”.

Maʼnosi: Allohim, uni qabr azobidan saqlagin.

Batafsil: https://telegra.ph/Janoza-namozi-03-25
Manba: muslim.uz, islom.uz
@islomuz_quron_bot
</b>""")


@dp.message_handler(text="Hayit namozi")
async def hayitnamoz(mes: Message):
    await mes.answer("""
<b>
HAYIT NAMOZI

1. «Alloh rizoligi uchun Ramazon (yoki Qurbon) hayiti namozini o'qishni niyat qildim. Yuzimni qibla tarafga qaratdim. Ushbu imomga iqtido qildim», deb niyat qilinadi.
2. Imom «Allohu akbar», deya takbir aytgach jamoat ham qo'llarini ko'tarib, ichida iftitoh takbirini aytadi.
3. Har kim ichida Sano duosini o'qiydi. So'ngra imom ketma-ket qo'llarini quloqlariga ko'tarib, uch marta takbir aytadi. Jamoat ham unga ergashadi. Birinchi va ikkinchi takbirda qo'llar yon tomonga tushiriladi. Uchinchi takbirdan so'ng qo'llar bog'lanib, qiyom holida turiladi.
4. Shundan keyin imom ichida «A'uzu»ni va «Bismillah»ni aytib, ovoz chiqarib Fotiha surasini va zam surani o'qiydi.
5. Ruku va sajdadan so'ng ikkinchi rakatga turiladi. Imom Fotiha surasi bilan bir kichik sura o'qigach, rukuga bormay turib, xuddi birinchi rakatdagi kabi uch marta takbir aytadi. To'rtinchi takbirdan keyin qo'llar bog'lanmasdan rukuga ketiladi va sajdalar ado etiladi. Sajdadan so'ngra «Attahiyyat» va «Salovot» o'qib, salom berilib, namoz tugatiladi.

Batafsil: https://telegra.ph/Hayit-namozlari-03-25
Manba: muslim.uz, islom.uz

@islomuz_quron_bot
</b>""")


@dp.message_handler(text="Istisqo namozi")
async def istisqo(mes: Message):
    await mes.answer("""
<b>
ISTISQO NAMOZI
Yomgʻir (suv) soʻrab oʻqiladigan namozning nomi “istisqo” deyiladi. Istisqo namozi deb suvga muhtoj boʻlib qolinganda Alloh taolodan bandalarining yomgʻir talab qilib oʻqiladigan namoziga aytiladi. Buni yashayotgan joylarining suvidan ekinlariyu hayvonlarini sugʻorib turgan, daryo, anhor va buloqlari boʻlmagan odamlar oʻqishadi. Mabodo, anhor va buloqlari boʻlsa ham, ehtiyojlariga yetmayotgani sababli ushbu namoz oʻqiladi.

Istisqo namozi xuddi ikki hayit namozi kabi ado qilinadi, lekin bunda zoida takbirlar aytilmaydi. Namoz oʻqib boʻlingach, yerda oʻzaro turib ikkita xutba oʻqish mustahab amallardandir. Ammo hayit namozlaridek minbarga chiqib xutba oʻqish makruhdir. Hayit namozidagi xutba takbirlari oʻrniga imom istigʻfor aytadi. Ikki xutbaning oʻrtasini bir oz oʻtirish bilan ajratadi. Imomning xutba mobaynida qibla tomonga yuzlanib turishi mandubdir. Xutbadan bir oz keyin imom kiyimini teskarisiga agʻdarib kiyib oladi va tasbeh aytib, moʻminlar va moʻminalar haqqiga istigʻfor aytadi. Lekin imomga ergashgan insonlar kiyimlarini teskarisiga agʻdarib kiymaydilar. Keyin imom odamlar tomoniga yuzlanib, tik turgan holida quyida keladigan istisqo duosini oʻqiydi, odamlar esa qiblaga yuzlanib oʻtirishadi va imomning duosiga “omin” deyishadi:

اللَّهُمَّ أَغِثْنَا، اللَّهُمَّ أَغِثْنَا، اللَّهُمَّ أَغِثْنَا، اللَّهُمَّ سُقْيَا رَحْمَةٍ، وَلَا سُقْيَا عَذَابٍ، وَلَا مَحْقٍ وَلَا بَلَاءٍ، وَلَا هَدْمٍ. اللَّهُمَّ عَلَى الظِّرَابِ وَمَنَابِتِ الشَّجَرِ، وَبُطُونِ الْأَوْدِيَةِ. اللَّهُمَّ حَوَالَيْنَا وَلَا عَلَيْنَا. اللَّهُمَّ اسْقِنَا غَيْثًا مُغِيثًا، هَنِيئًا مَرِيئًا، غَدَقًا مُجَلِّلًا، سَحًّا، عَامًّا طَبَقًا دَائِمًا. اللَّهُمَّ اسْقِنَا الْغَيْثَ، ولَا تَجْعَلْنَا مِنَ الْقَانِطِيْنَ. اللَّهُمَّ أَنْبِتْ لَنَا الزَّرْعَ، وَأَدِرَّ لَنَا الضَّرْعَ، وَأَنْزِلْ عَلَيْنَا مِن بَرَكَاتِ الْأَرْضِ، وَاكْشِفْ عَنَّا مِنَ الْبَلَاءِ مَا لَا يَكْشِفُهُ غَيْرُكَ. اللَّهُمَّ اسْقِ عِبَادَكَ وَبَهَائِمَكَ، وَانْشُرْ رَحْمَتَكَ، وَأَحْيِ بَلَدَكَ الْمَيِّتَ. اللَّهُمَّ اَنْتَ اللهُ لَا إلَهَ إلَّا اَنْتَ، أَنْتَ الْغَنِيُّ وَنَحْنُ الْفُقَرَاءُ، أَنْزِلْ عَلَيْنَا الْغَيْثَ، وَاجْعَلْ مَا أَنْزَلْتَ لَنَا قُوَّةً وَبَلَاغًا إِلَى حِينٍ. اللَّهُمَّ إِنَّا نَسْتَغْفِرُكَ إِنَّكَ كُنْتَ غَفَّارًا، فَأَرْسِلِ السَّمَاءَ مِدْرَارًا.



“Allohumma agʻisna, Allohumma agʻisna, Allohumma agʻisna. Allohumma suqya rohmatin vala suqya azobin vala mahqin vala baloin vala hadmin. Allohumma ʼalaz zirobi va manabitish shajari va butunil avdiyati. Allohumma havolayna vala ʼalayna. Allohummasqina gʻoysan mugʻiysan haniyʼan mariyʼan gʻodaqon mujallilan sahhan omman tobaqan daiman. Allohummasqinal gʻoysa vala tajʼalna minal qonitiyn. Allohumma anbit lanaz zarʼa va adirra lanad darʼa va anzil ʼalayna min barokatil ardi vakshif ʼannaa minal baloi maa laa yakshifuhu gʻoyruka. Allohummasqi ʼibodaka va bahoimaka vanshur rohmataka vaahyi baladakal mayyita. Allohumma antallohu la ilaha illa anta antal gʻoniyyu va nahnul fuqarou anzil ʼalaynal gʻoysa vajʼal ma anzalta lana quvvatan va balagʻan ila hiyn. Allohumma inna nastagʻfiruka innaka kunta gʻoffaro, faarsilis samaa ʼlayna midroro”.

Yomgʻir talab qilib oʻqiladigan namoz uchun oʻz maskanlaridan chetroqqa uch kun ketma-ket chiqish mustahabdir. U yerga ahli zimmiylar (yaʼni Islom yurtida yashash evaziga tovon toʻlovchi boshqa din vakillari) olib chiqilmaydi. Har kun chiqishdan oldin musulmonlar tavbalarini yangilab, zulmlariga tavba qilib, beva-bechoralarga sadaqa qilishlari ham mustahab amallardandir. Har bir musulmon yer yuzidagi barcha musulmon birodarlari haqqiga istigʻfor aytadi.

Batafsil: https://telegra.ph/Istisqo-namozi-03-25
Manba: islom.uz

@islomuz_quron_bot
</b>""")


@dp.message_handler(text="Kusuf namozi")
async def kusuf(mes: Message):
    await mes.answer("""
<b>
QUYOSH VA OY TUTILGANDAGI NAMOZLAR
Quyosh tutilgan vaqtda ikki yoki toʻrt va yo undan koʻproq namoz (kusuf namozi) oʻqish sunnatdir. Afzali bir yoki ikki salom bilan toʻrt rakat oʻqishdir. Kamida esa ikki rakatli nafl namoz koʻrinishida oʻqiladi. Bu namoz jamoat boʻlib, azon va iqomatsiz, qiroatni jahriy qilmay va xutba oʻqimasdan ado qilinadi. Insonlarni jamoatga toʻplash uchun jamoat namoziga deb chaqiriladi. 

Quyosh tutilganda oʻqiladigan namozni juma namozida imomlik qiladigan kishi imom boʻlib oʻqib berishi lozim. Agar u boʻlmasa, sultonning ruxsati bilan tayin qilingan kishi oʻqib berishi kerak. Agar bular ham boʻlmasa, insonlar oʻzlari yolgʻiz-yolgʻiz boʻlib, oʻz manzillarida oʻqishadi. Ushbu namozning birinchi rakatida Fotihadan soʻng Baqara surasi kabi, ikkinchi rakatida Oli Imron surasi kabi uzun suralarni qiroat qilish sunnatdir. Agar rakatdagi qiroatlarni yengil qilsa, namozdan keyingi duoni uzun qiladi. Hadisi sharifda kelishicha, muhimi insonlar quyosh tutilgan vaqtda namoz va duo bilan mashgʻul boʻlishlari kerak. Agar qiroatni uzun qilsalar, duoni qisqa qiladilar, duoni uzun qilsalar, qiroatni qisqa qiladilar. Toki quyoshning tutilishi yoʻqolguncha namoz va duoga mashgʻul boʻladilar. Rukuʼ-sajdalarni ham behad uzun qilishadi. Imom qiblaga yuzlanib oʻtiradi va xohlagancha duo qiladi, odamlar esa duoga qoʻl ochib “omin” deb turadilar. 

  Oy tutilganda oʻqiladigan namoz ham xuddi quyosh tutilganda oʻqiladigan namoz kabidir. Lekin bu namozni oʻqish mustahab boʻlib, uni masjidda yigʻilib, jamoat holida oʻqish shariatda yoʻlga qoʻyilmagan, balki har kim oʻz uyida yolgʻiz-yolgʻiz boʻlib ado qiladi. Quyosh va oy tutilganda oʻqiladigan namozlar biror dahshatli voqea sodir boʻlganda ham oʻqiladi. Misol uchun, qattiq zilzilalar, bir voqea sabab koʻpchilikning oʻlib ketishi, shiddatli shamollar, kunduz kuni atrofni qoʻrqinchli qorongʻulik oʻrab olishi va shu kabi vahimaga soladigan hodisalar sodir boʻlishi bilan namoz oʻqish, gunohlardan chetlanish, insonlar oʻzlarini toʻgʻrilashlari va najot topishlari uchun sabab boʻladigan ibodatlarga qaytishlari odatiy holdir. Ibodatlardan uzoqlashib, gunoh koʻchasiga kirib qolgan bandani Robbisiga qaytarib, Unga yaqinlashtiradigan eng yaxshi ibodat namozdir.

Batafsil: https://telegra.ph/Kusuf-namozi-03-25
Manba: islom.uz

@islomuz_quron_bot
</b>
""")


@dp.message_handler(text="Taroveh namozi")
async def taroveh(mes: Message):
    await mes.answer("""
<b>
TAROVEH NAMOZI
Taroveh – “orom oldirish, dam berish” maʼnolaridagi “tarveha” soʻzining koʻplik shaklidir. Ramazon oyida xufton namozidan soʻng va vitr namozi oldidan oʻqiladigan namozga “taroveh” deyiladi. Uning har toʻrt rakatidan soʻng dam olingani uchun shunday nom berilgan. Taroveh namozi yigirma rakat boʻlib, sunnati muakkadadir.

Rasululloh sollallohu alayhi vasallam: “Kim Allohdan savob umid qilib ramazon namozini (tarovehni) oʻqisa, oldingi gunohlari kechiriladi”, deganlar

Imom Buxoriy va Muslim rivoyat qilgan.

Taroveh namozini jamoat boʻlib oʻqish esa mahalla kishilari uchun sunnati kifoya hisoblanadi. Yaʼni baʼzilar jamoat boʻlib tarovehni oʻqishsa, qolganlardan jamoat boʻlib oʻqish sunnati soqit boʻladi. Ammo bir mahallada hech kim jamoat boʻlmasa, shu mahalladagi hamma odam sunnatni tark qilgan hisoblanadi.

Hazrati Umar roziyallohu anhu oʻzlarining xalifalik davrlarida odamlarning ramazon kechalarida masjidga toʻplab, tarovehni yigirma rakat jamoat bilan oʻqishni joriy qildilar. Sahobalardan biror kishi bu ishga qarshi chiqmadi. Rasululloh sollallohu alayhi vasallam muborak hadisi shariflarida shunday marhamat qilganlar: “Oʻzinglarga mening sunnatimni hamda roshid va mahdiy boʻlgan (yaʼni hidoyat, toʻgʻri yoʻldan yuruvchi) xalifalarimning sunnatini lozim tutinglar, buni aql tishlaring bilan mahkam tishlab olinglar” (Abu Dovud rivoyat qilgan). 

Abu Hanifaning shogirdlaridan boʻlgan Abu Yusuf ustozidan: “Nima uchun Umar roziyallohu anhu bu ishni qilgan?” deb soʻradi. Abu Hanifa: “Taroveh – sunnati muakkadalardandir. Umar roziyallohu anhu bu ishni oʻzidan oʻylab chiqib joriy qilgani yoʻq. U hargiz bidʼatchilardan boʻlmagan. U musulmonlarni nimaga buyurgan boʻlsa, oʻzi bilgan dindagi asl narsaga, Rasululloh sollallohu alayhi vasallam zamonlarida bor boʻlgan amalga buyurgan”, deb javob berdilar.

Taroveh namozi vitrdan tashqari yigirma rakat hisoblanadi. Uning vaqti xufton namozidan keyin kirib, to bomdod vaqti kirguncha davom etadi. Vitrdan oldin ham, keyin ham oʻqish durust boʻladi. Lekin afzali tarovehni vitrdan oldin oʻqishdir. Taroveh ikki rakatdan oʻqiladi, har toʻrt rakat oʻqilgach, bir oz istirohat uchun oʻtirish maʼquldir. Sahobai kiromlar ham xuddi shunday qilishardi. Taroveh (istirohat) namozi, deb nomlanishining ham asl sababi shudir. Chunki taroveh rohatlanish maʼnosidadir. Namozxon shu oʻtirishda zikru tasbehga mashgʻul boʻladi yoki sukut saqlaydi.

Taroveh namozlarida Qurʼoni Karimni bir bora xatm qilib chiqish ham ramazon oyining sunnat amallaridandir. Afzali imom jamoatning holiga rioya qilib qiroatni bir oz tezlatadi, lekin shart shuki, tezlik namozni buzadigan yoki namozxonlar anglay olmay qoladigan darajada boʻlmasin. Bordi-yu taroveh namozlarida Qurʼoni Karimni xatm qilishdan qavm malollanguday boʻlsa, imom ularning malollanishini eʼtiborga olmaydi, balki sunnatni ado qiladi. Fotihadan keyingi zam surani uzun oyatdan bir oyat, qisqa oyatdan uch oyat miqdoridan kam oʻqib qoʻyish haromga yaqin makruhlardan hisoblanadi. Chunki bunda vojibni tark qilish bor. Tarovehning har ikki rakati mustaqil namoz boʻlib, ularga alohida niyat qilinadi, takbiri tahrimadan soʻng esa sano va “Aʼuzu...”, “Bismillah...”lar oʻqiladi. Qaʼdada tashahhudga qoʻshimcha salavot va duolarni ham qoʻshadi va hokazo.

Taroveh namozlarini qiyomga qodir boʻlaturib oʻtirib oʻqish ham durustdir. Ammo qiyomda turib oʻqisa, oʻtirib oʻqigandan koʻra afzalroq boʻladi. Imomga ergashuvchi oʻtirgan holida ham iqtido qilsa durust, ammo qiyomga qodir boʻlaturib, to imom rukuʼga borguncha qiyomni kechiktirish makruh hisoblanadi. Chunki bunda ibodatga dangasalik qilgani zohir boʻladi. Taroveh namozining masjidda ado qilinishi maʼquldir. Zero, shariatga koʻra, jamoat boʻlib ado qilinadigan ibodatlarning afzalrogʻi masjidda boʻlganidir. 

Batafsil: https://telegra.ph/Taroveh-namozi-03-25
Manba: islom.uz

@islomuz_quron_bot
</b>""")


@dp.message_handler(text="Nafl namozlar")
async def nafl(mes: Message):
    await mes.answer("""
<b>
NAFL NAMOZLAR
“Nafl namozi” deb kishi oʻz ixtiyori bilan farzga qoʻshimcha tarzda oʻqiydigan namozga aytiladi. Bu namozni Alloh taolo moʻminlar zimmasiga farz kabi majburiy qilmagan, balki ixtiyoriy suratda ado etilsa, savob boʻladi. 

Nafl namozlari ikki xil boʻladi: 

1. Besh vaqt farz namozlariga tobe boʻlgan nafllar. Bular farzlardan oldin yoki keyin oʻqiladigan namozlar boʻlib, ular “sunnati ravotiblar” deyiladi. 

2. Besh vaqt namozlardan tashqari mustaqil oʻqiladigan namozlar. Bular jumlasiga zuho, tahajjud, istixora, tavba, tasbeh, tahiyyatul masjid, shukri vuzu`, hojat soʻrash va boshqa namozlar kiradi.

Batafsil: https://telegra.ph/Nafl-namozlar-03-25
Manba: islom.uz

@islomuz_quron_bot
</b>""")


@dp.message_handler(text="Musofirning namozi")
async def musofir(mes: Message):
    await mes.answer("""
<b>
MUSOFIRNING NAMOZI
Piyoda oʻrtacha yurganda uch kechayu uch kunduzlik yoʻlni bosib yetadigan joyga safarga chiqqan kishi yashaydigan joyi hududidan chiqishi bilan qaytib kelgunicha “musofir” hisoblanadi (bu hanafiy mazhabida 96 kilometrga, boshqa mazhablarda 88 kilometrga teng). “Oʻrtacha yurish” deganda tuya va piyoda kishining yurishi kabilarga aytiladi. Ushbu masofadan kamroq yerga yoʻl olgan kishi musofir hisoblanmaydi. Ana shu masofadagi yerga mashinada, poyezdda, samolyotda yoʻlga chiqqanlar ham musofir hisoblanadi. U joyda oʻn besh kundan kamroq muddat turishni niyat qilgan boʻlsayu, oylab-yillab qolib ketsa ham, musofir sanalaveradi. Agar borgan joyida oʻn besh kun yoki undan koʻp muddat turishni niyat qilsa, yetib borgach musofir hisoblanmaydi.

Musofir kishi safarda toʻrt rakatli farz namozlarini ikki rakat qilib qisqartirib (qasr qilib) oʻqiydi. Ular peshin, asr, xuftondir. Ammo bomdod, shom va vitr namozlari hamda sunnati ravotiblar esa butun oʻqiladi. Musofir tahorat olgach, mahsisiga uch kechayu uch kunduz masʼh etishi mumkin.

Agar musofir yoʻl yurib turgan boʻlsa, vaqti ziq, sharoit yoʻqligi uchun sunnatlarni oʻqimasligi afzaldir. Ammo shunda ham bomdodning sunnatini tark qilmay oʻqiydi. Agar musofir bir manzilga kelib tushsa, vaqt bemalol, sharoit yetarli boʻlgani uchun sunnatlarni oʻqishi afzal boʻladi. Safarda sunnat namozlarini oʻqish yoki oʻqimaslik borasida izlanish qilgan ulamolar ushbu xulosani aytishgan.

Musofirga namozni qasr qilish vojibdir. Butun qilib oʻqish joiz emas, mabodo, butun qilib oʻqisa, gunohkor boʻladi. Chunki u qaʼdai oxirdan keyingi salomni kechiktirdi. Musofirning shu holda ikkinchi rakatdan keyingi oʻtirishi qaʼdai oxir hisoblanadi. Agar qasr qilmay, toʻrt rakat oʻqisa, keyingi ikki rakati nafl hisoblanadi. Ushbu naflni takbiri tahrimasiz boshlagan, sano bilan “aʼuzu...”ni ham tark qilgan boʻladi. Agar oʻrtadagi qaʼdani tashahhud miqdoricha oʻtirmay, uchinchi rakat va toʻrtinchi rakatni ado qilgan boʻlsa, farz namozi botil boʻlib, uni qayta oʻqish vojib boʻladi. Chunki musofirning ikkinchi rakatdan keyin qaʼdaga oʻtirishi farz edi. Agar musofir qasr namozini butun qilib oʻqiyotgan boʻlsa, unga ikkinchi rakatdan keyingi rakatlarda oʻsha farz namozini oʻquvchi kishining iqtidosi durust emas. Chunki farz oʻquvchining nafl oʻquvchiga iqtido qilishi joiz boʻlmaydi.

Batafsil: https://telegra.ph/Musofirning-namozi-03-25
Manba: islom.uz, muslim.uz

@islomuz_quron_bot
</b>""")


@dp.message_handler(text="Bemorning namozi")
async def bemornamozi(mes: Message):
    await mes.answer("""
<b>
BEMOR KISHINING NAMOZI
Islom yengillik dinidir. Bu dinda musulmonlar noilojlikka, mashaqqatga solib qoʻyilmaydi, ular qodir boʻlmaydigan ibodatlarga buyurilmaydi. Shu bilan birga Islomda namozga qattiq eʼtibor beriladi va uni ado qilish uchun turli choralar yoʻlga qoʻyiladi. Bemor kishi qiyom turishdan ojiz boʻlsa yoki kasali kuchayib ketishidan xavf qilsa yo shifoning kechikishiga shu qiyom turishi sabab boʻlsa, u holda oʻtirib namoz oʻqiydi. Lekin rukuʼ va sajdalarni toʻla qiladi. Agar rukuʼ va sajdaga ham qodir boʻlmasa, xuddi tashahhudda oʻtirgani kabi chap oyogʻini toʻshab, oʻng qadamini tik qilgan holda oʻtiradi. Bu eng afzalidir. Agar bunga ham qodir boʻlmasa, xohlagan suratda oʻtiradi va rukuʼ hamda sajdalarni boshi bilan ishora qiladi. Bunda rukuʼ uchun boshini ozroq egsa, sajda uchun koʻproq egadi. 

Agar sajdaga ojiz boʻlaturib rukuʼga qodir boʻlsa ham, baribir ikkisi uchun ishora qiladi. Sajdaga imkoni yoʻq kasalning ishora bilan qilgan sajdasi kifoya qiladi. Ammo uning sajda qilishi uchun biror narsani yuzi barobar koʻtarib qoʻyish joiz emas. Imo-ishora bilan namoz oʻqish tik turgan holda ham, oʻtirgan holda ham durustdir. Lekin bemor kishining oʻtirib, imo-ishora bilan namoz oʻqishi afzal hisoblanadi. Agar sajda qilishga ojiz boʻlsa, undan qiyom turish ham soqit boʻladi. 

Agar bemorga oʻtirish ham mashaqqat boʻlsa, u oʻng tomon bilan qiblaga yuzlangan holda yonboshlab yotadi, shu afzalidir. Boʻlmasa, chalqanchasiga yotib, oyoqlarini qibla tomonga uzatadi, tizzasini esa bir oz bukib oladi. Boshni bir oz koʻtarish uchun orqaga yostiq qoʻyiladi. Bu holat yonboshlashdan koʻra afzalroqdir. Shu holda imo-ishora qilib namozni oʻqiydi. Agar bunday turishga ham qodir boʻlmasa, oʻziga qulay boʻlgan suratda oʻrnashib, ishora bilan namozini oʻqiydi. Kiyimi va joyi najosat boʻlsa, agar namozni ado qilgunicha yana qayta najosat boʻlsa, almashtirmay oʻqiyveradi. Agar namozni ado qilgunicha pok tursa, kiyim va joyini poklab oʻqiydi. 

Agar sogʻlom kishi namoz asnosida kasal boʻlib, ogʻriqdan qiyomga qodir boʻlmay qolsa, oʻsha zahoti oʻtirib, ishora bilan namozni tugatadi. Agar oʻtirishga ham majoli kelmay qolsa, unda chalqanchasiga yotadi va namozni ishora bilan oxiriga yetkazadi. Ishora faqat bosh bilan qilinadi. Agar boshini qimirlata olmay qolsa, koʻz yoki qosh bilan ishora qilmaydi hamda qalbi bilan ham namozning arkonlarini ijro etmaydi, balki ushbu holda namozni kechiktiradi va tuzalgandan keyin esa qazosini oʻqib qoʻyadi. 

Agar bemor kishiga oʻtirib ham namoz oʻqish uzrli boʻlsa, bu paytda u yonboshlab, qiblaga yuzlangan holda yoki orqasi bilan yotib namoz oʻqiydi. Lekin orqasi bilan yotib ishora qilishi yaxshiroqdir. Betob kishiga bosh bilan ishora qilish ham mumkin boʻlmasa, namoz toʻxtatib turiladi. 

Ishora bilan namoz oʻquvchi kishi namoz ichida tuzalib qolsa, namozini boshidan qayta oʻqiydi. Rukuʼ va sajdalarni oʻtirgan holda ado etayotgan namozxonning salomatligi namoz oʻrtasida yaxshilanib qolsa, qolgan namozlarini tik turgan holatda davom ettiradi. 

Suzayotgan kemada namoz oʻqiyotgan kishi hech qanday uzrsiz ham namozini oʻtirib oʻqishi mumkin. 

Qirgʻoqqa bogʻlab qoʻyilgan va toʻxtab turgan kemalarda esa namozxon ibodatini tik turgan holatda ado etadi. Agar uzrli boʻlsa, oʻtirib oʻqiydi. 

Namozxon bir kechayu bir kunduz ichida hushdan ketgan boʻlsa yoki jinni boʻlib tursa, oʻqishga qodir boʻlmagan namozlarining qazosini ado etadi. Hushdan ketishi yoki jinniligi bir kecha-kunduzdan ziyoda boʻlsa, qoldirgan namozlari qazosini oʻqishi lozim boʻlmaydi. Dori vositasida hushidan ketkazilgan boʻlsa, Abu Hanifa rohmatullohi alayh “Bir kecha kunduzdan oshsa ham qazosini oʻqiydi” deganlar.

Batafsil: https://telegra.ph/Bemor-kishining-namozi-03-25
Manba: islom.uz

@islomuz_quron_bot
</b>""")


@dp.message_handler(text="Tilovat sajdasi")
async def tilovatsajdasi(mes: Message):
    await mes.answer("""
<b>
TILOVAT SAJDASI
Qurʼoni Karimning oʻn toʻrtta surasidagi (baʼzi mazhablarda Haj surasining ikki joyida deb hisoblanadi) sajda oyatlari oʻqilganida yoki boshqaning ogʻzidan eshitilganda qilinadigan sajda amali “tilovat sajdasi” deyiladi.

Sajda oyatlarini oʻquvchi ham, eshituvchi ham sajda qilishi vojib boʻladi. Uning vojib boʻlishi sharti namoz vojib boʻlishidagi ahliylik kabidir. Ahliylik – musulmon, balogʻat yoshiga yetgan, tahoratli (hayz, nifosdan pok) boʻlishdir. Sajda oyatlaridan biri oʻqilgach, uni eshituvchi va oʻquvchi uchun baʼzan keng vaqtda va baʼzida tez fursatda sajda qilib olish vojibdir. Agar sajda oyati namozdan tashqarida oʻqilsa va yoki eshitilsa, uni bajarish uchun fursat kengroq boʻlsa, kechiktirgan kishi gunohkor boʻlmaydi. Ammo hayotining oxirigacha kechiktirib, sajda qila olmay vafot etsa gunohkor boʻladi. Uni kechiktirishning hukmi yengil makruhdir. Agar sajda oyati namoz ichida tilovat qilinsa, bu holda uni ado etishni kechiktirib boʻlmaydi, balki vaqt oʻtkazmay, sajda qilish vojib boʻladi.

Batafsil: https://telegra.ph/Tilovat-sajdasi-03-25
Manba: islom.uz

@islomuz_quron_bot
</b>""")


@dp.message_handler(text="Ibratli namozlar")
async def ibratlinamozlar(mes: Message):
    await mes.answer("""
<b>
Abdulloh ibn Masʼud roziyallohu anhu dedilar: “Bir kecha men janobi Rasululloh (sollallohu alayhi vasallam) bilan namoz oʻqidim. Janob qiyomda shu qadar uzoq turdilarki, men tahammul qila olmay, oʻltirib olmoqchi va janob Rasulullohning oʻzlarini tanho qoʻymoqchi boʻldim”. 

Hazrat Oisha roziyallohu anho shunday dedilar: “Janobi Rasuli akram sollallohu alayhi vasallam oxirgi paytlarda nafl namozlarini oʻtirib oʻqidilar. Oʻtirgan hollarida Qurʼoni sharifni odatlariga muvofiq uzun oʻqib borardilar. Vaqtiki, bir rakatning hissasidan oʻttiz yoki qirq oyat miqdori qolsa, shunda turib olardilar. Keyin rukuʼ va sajda qilardilar. Keyin ikkinchi rakatda ham shunday qilardilar”. 

Avf ibn Molik roziyallohu anhu shunday deganlar: “Bir kecha men janobi Rasululloh sollallohu alayhi vasallam bilan birga boʻldim. U zot avval misvok ishlatdilar, keyin tahorat oldilar. Keyin namozga niyat qildilar. Men ham u zotga iqtido qilib, namozga shuruʼ qildim. Janob surai Fotihadan soʻng zam suraga Baqara surasini boshladilar. Qachon bir rahmat oyatini oʻqisalar, toʻxtab olib, Allohdan rahmat talab etardilar. Qachon bir azob oyatini oʻqisalar, toʻxtab turib, undan panoh tiladilar. Keyin rukuʼ qildilar. Va rukuʼlarida qiyomda turgan mikdorcha turdilar va: «Subhana zil jabarutu val malakut val kibriyai val azamati” duosini oʻqidilar. Keyin sajda qildilar va sajdaga ham rukuʼda turgan mikdorda turdilar va bunda ham yuqoridagi duoni oʻqib turdilar. Keyin ikkinchi rakatga turdilar va bunda Oli Imronni zam qildilar. Va bu rakatda ham avvalgi holatni qaytardilar. Bu namoz oʻzi toʻrt rakatli namoz edi. Uchinchi rakatida Niso surasini, toʻrtinchisida Moida surasini oʻsha kayfiyatda oʻqidilar». 

Bir kishi Oisha roziyallohu anhodan soʻradi: “Paygʻambar sollallohu alayhi vasallam haqida birorta diqqatga sazovor hadis ayting”. U kishi shunday javob berdilar: “Rasulullohning hech bir narsalari gʻayritabiiy emas edi. Har bir qilgan ishlari diqqatga sazovor edi. Bir kuni tunda kelib, men bilan yotdilar. Bir ozdan keyin: «Endi men Egamga ibodat qilay”, deb turib ketdilar. Shunday deb, Nabiy namozga turdilar, Yaratguvchi oldida samimiyat bilan kamtarona qiyomga turdilar, koʻz yoshlari yonoqlaridan soqollariga va koʻksilariga oqib tushdi. Undan keyin rukuʼ va sajdaga egilganlarida koʻz yoshlari xuddi oldingidek duvillab oqdi. Sajdadan bosh koʻtargach, Bilol fajr namozi yaqinlashib qolganini maʼlum qilgunicha yigʻini davom ettirdilar. Men u zot bilan birga Allohdan rahm-shafqat tiladim va: “Ey Allohning Rasuli! Siz begunohsiz, chunki Alloh fazli-karami bilan sizning avval qilgan va kelgusida keladigan barcha gunohlaringizni kechirgan-ku, yana siz Undan mamnun emasmisiz?” dedim. Rasululloh javob berdilar: “Nega endi men – Allohning quli mamnun boʻlmayin?” Keyin qoʻshimcha qildilar: “Nega men bunday ibodat qilmasligim kerak? Alloh bugungi kunda menga ushbu oyatlarni nozil qildi-ku: «Albatta, osmonlaru Yerning yaratilishida hamda kecha va kunduzning almashib turishida aql egalari uchun oyat (belgi)lar bor. Ular Allohni tik turgan, oʻtirgan va yonboshlagan hollarida zikr qiladilar va osmonlaru Yerning yaratilishi haqida tafakkur qilib, shunday deydilar: «Robbimiz, buni bekorga yaratganing yoʻq, Oʻzing poksan, bizni olov azobidan saqlagin” (Oli Imron surasi, 190-191-oyatlar)».
        
Davomi: https://telegra.ph/Ibratli-namozlar-03-25
Manba: islom.uz

@islomuz_quron_bot
</b>""")
