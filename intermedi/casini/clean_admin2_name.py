__author__ = 'silvia.calo'
#correct the names of admin2 names in emdat_record_list, using nested list comprehensions
def clean(emdat_record_list):
    emdat_record_clean = []

    bangladesh = []
    for row in range(0,len(emdat_record_list)):
        if emdat_record_list[row][3]=='bangladesh':
            bangladesh.append(emdat_record_list[row])
            bangladesh1 = [bangladesh[row][10].replace('area','')for row in range(0,len(bangladesh))]
            bangladesh2 = [bangladesh1[row].replace('districts','')for row in range(0,len(bangladesh1))]
            bangladesh3 = [bangladesh2[row].replace('district','')for row in range(0,len(bangladesh2))]
            bangladesh4 = [bangladesh3[row].replace('near','')for row in range(0,len(bangladesh3))]
            bangladesh5 = [bangladesh4[row].replace('north','')for row in range(0,len(bangladesh4))]
            bangladesh6 = [bangladesh5[row].replace('regions','')for row in range(0,len(bangladesh5))]
    bangladesh_clean = list(bangladesh)
    for row in range(0,len(bangladesh6)):
        bangladesh_clean[row][10] = bangladesh6[row]
    for row in bangladesh_clean:
        emdat_record_clean.append(row)

    colombia = []
    for row in range(0,len(emdat_record_list)):
        if emdat_record_list[row][3]=='colombia':
            colombia.append(emdat_record_list[row])
            colombia1 = [colombia[row][10].replace('isl.','')for row in range(0,len(colombia))]
    colombia_clean = list(colombia)
    for row in range(0,len(colombia1)):
        colombia_clean[row][10] = colombia1[row]
    for row in colombia_clean:
        emdat_record_clean.append(row)

    cuba = []
    for row in range(0,len(emdat_record_list)):
        if emdat_record_list[row][3]=='cuba':
            cuba.append(emdat_record_list[row])
            cuba1 = [cuba[row][10].replace('provinces','')for row in range(0,len(cuba))]
            cuba2 = [cuba1[row].replace('province','')for row in range(0,len(cuba1))]
            cuba3 = [cuba2[row].replace('municipality','')for row in range(0,len(cuba2))]
    cuba_clean = list(cuba)
    for row in range(0,len(cuba3)):
        cuba_clean[row][10] = cuba3[row]
    for row in cuba_clean:
        emdat_record_clean.append(row)

    el_salvador = []
    for row in range(0,len(emdat_record_list)):
        if emdat_record_list[row][3]=='elsalvador':
            el_salvador.append(emdat_record_list[row])
            el_salvador1 = [el_salvador[row][10].replace('province','')for row in range(0,len(el_salvador))]
            el_salvador2 = [el_salvador1[row].replace('departments','')for row in range(0,len(el_salvador1))]
    el_salvador_clean = list(el_salvador)
    for row in range(0,len(el_salvador2)):
        el_salvador_clean[row][10] = el_salvador2[row]
    for row in el_salvador_clean:
        emdat_record_clean.append(row)

    guatemala = []
    for row in range(0,len(emdat_record_list)):
        if emdat_record_list[row][3]=='guatemala':
            guatemala.append(emdat_record_list[row])
            guatemala1 = [guatemala[row][10].replace('departments','')for row in range(0,len(guatemala))]
            guatemala2 = [guatemala1[row].replace('provinces','')for row in range(0,len(guatemala1))]
            guatemala3 = [guatemala2[row].replace('costade','')for row in range(0,len(guatemala2))]
            guatemala4 = [guatemala3[row].replace('department','')for row in range(0,len(guatemala3))]
    guatemala_clean = list(guatemala)
    for row in range(0,len(guatemala4)):
        guatemala_clean[row][10] = guatemala4[row]
    for row in guatemala_clean:
        emdat_record_clean.append(row)

    guinea_bissau = []
    for row in range(0,len(emdat_record_list)):
        if emdat_record_list[row][3]=='guineabissau':
            guinea_bissau.append(emdat_record_list[row])
            guinea_bissau1 = [guinea_bissau[row][10].replace('province','')for row in range(0,len(guinea_bissau))]
    guinea_bissau_clean = list(guinea_bissau)
    for row in range(0,len(guinea_bissau1)):
        guinea_bissau_clean[row][10] = guinea_bissau1[row]
    for row in guinea_bissau_clean:
        emdat_record_clean.append(row)

    haiti = []
    for row in range(0,len(emdat_record_list)):
        if emdat_record_list[row][3]=='haiti':
            haiti.append(emdat_record_list[row])
            haiti1 = [haiti[row][10].replace('area','')for row in range(0,len(haiti))]
            haiti2 = [haiti1[row].replace('departments','')for row in range(0,len(haiti1))]
            haiti3 = [haiti2[row].replace('department','')for row in range(0,len(haiti2))]
            haiti4 = [haiti3[row].replace('south','')for row in range(0,len(haiti3))]
            haiti5 = [haiti4[row].replace('urbanregion','')for row in range(0,len(haiti4))]
    haiti_clean = list(haiti)
    for row in range(0,len(haiti5)):
        haiti_clean[row][10] = haiti5[row]
    for row in haiti_clean:
        emdat_record_clean.append(row)

    honduras = []
    for row in range(0,len(emdat_record_list)):
        if emdat_record_list[row][3]=='honduras':
            honduras.append(emdat_record_list[row])
            honduras1 = [honduras[row][10].replace('provinces','')for row in range(0,len(honduras))]
            honduras2 = [honduras1[row].replace('northcoast','')for row in range(0,len(honduras1))]
            honduras3 = [honduras2[row].replace('graciasdios','graciasadios')for row in range(0,len(honduras2))]
            honduras4 = [honduras3[row].replace('municipality','')for row in range(0,len(honduras3))]
            honduras5 = [honduras4[row].replace('departments','')for row in range(0,len(honduras4))]
            honduras6 = [honduras5[row].replace('department','')for row in range(0,len(honduras5))]
    honduras_clean = list(honduras)
    for row in range(0,len(honduras6)):
        honduras_clean[row][10] = honduras6[row]
    for row in honduras_clean:
        emdat_record_clean.append(row)

    india = []
    for row in range(0,len(emdat_record_list)):
        if emdat_record_list[row][3]=='india':
            india.append(emdat_record_list[row])
            india1 = [india[row][10].replace('province','')for row in range(0,len(india))]
            india2 = [india1[row].replace('districts','')for row in range(0,len(india1))]
            india3 = [india2[row].replace('east&','eastgodavari')for row in range(0,len(india2))]
            india4 = [india3[row].replace('eastmadhyapradesh','madhyapradesh')for row in range(0,len(india3))]
            india5 = [india4[row].replace('nw.','')for row in range(0,len(india4))]
            india6 = [india5[row].replace('states','')for row in range(0,len(india5))]
            india6a = [india6[row].replace('state','')for row in range(0,len(india6))]
            india7 = [india6a[row].replace('eastuttarpradesh','')for row in range(0,len(india6a))]
            india8 = [india7[row].replace('district','')for row in range(0,len(india7))]
            india9 = [india8[row].replace('coastal','')for row in range(0,len(india8))]
            india10 = [india9[row].replace('karaikalregion','karaikal')for row in range(0,len(india9))]
            india11 = [india10[row].replace('level1=','')for row in range(0,len(india10))]
            india12 = [india11[row].replace('gujaratcoast','gujarat')for row in range(0,len(india11))]
            india13 = [india12[row].replace('cuddalorecoast','cuddalore')for row in range(0,len(india12))]
    india_clean = list(india)
    for row in range(0,len(india13)):
        india_clean[row][10] = india13[row]
    for row in india_clean:
        emdat_record_clean.append(row)

    indonesia = []
    for row in range(0,len(emdat_record_list)):
        if emdat_record_list[row][3]=='indonesia':
            indonesia.append(emdat_record_list[row])
            indonesia1 = [indonesia[row][10].replace('district','')for row in range(0,len(indonesia))]
    indonesia_clean = list(indonesia)
    for row in range(0,len(indonesia1)):
        indonesia_clean[row][10] = indonesia1[row]
    for row in indonesia_clean:
        emdat_record_clean.append(row)

    iran = []
    for row in range(0,len(emdat_record_list)):
        if emdat_record_list[row][3]=='iran':
            iran.append(emdat_record_list[row])
            iran1 = [iran[row][10].replace('provinces','')for row in range(0,len(iran))]
    iran_clean = list(iran)
    for row in range(0,len(iran1)):
        iran_clean[row][10] = iran1[row]
    for row in iran_clean:
        emdat_record_clean.append(row)

    north_korea = []
    for row in range(0,len(emdat_record_list)):
        if emdat_record_list[row][3]=='northkorea':
            north_korea.append(emdat_record_list[row])
            north_korea1 = [north_korea[row][10].replace('city','')for row in range(0,len(north_korea))]
            north_korea2 = [north_korea1[row].replace('districts','')for row in range(0,len(north_korea1))]
            north_korea3 = [north_korea2[row].replace('provinces','')for row in range(0,len(north_korea2))]
            north_korea4 = [north_korea3[row].replace('province','')for row in range(0,len(north_korea3))]
            north_korea5 = [north_korea4[row].replace('south','')for row in range(0,len(north_korea4))]
            north_korea6 = [north_korea5[row].replace('north','')for row in range(0,len(north_korea5))]
            north_korea7 = [north_korea6[row].replace('west','')for row in range(0,len(north_korea6))]
            north_korea8 = [north_korea7[row].replace('east','')for row in range(0,len(north_korea7))]
    north_korea_clean = list(north_korea)
    for row in range(0,len(north_korea8)):
        north_korea_clean[row][10] = north_korea8[row]
    for row in north_korea_clean:
        emdat_record_clean.append(row)

    laos = []
    for row in range(0,len(emdat_record_list)):
        if emdat_record_list[row][3]=='laos':
            laos.append(emdat_record_list[row])
            laos1 = [laos[row][10].replace('provinces','')for row in range(0,len(laos))]
    laos_clean = list(laos)
    for row in range(0,len(laos1)):
        laos_clean[row][10] = laos1[row]
    for row in laos_clean:
        emdat_record_clean.append(row)

    madagascar = []
    for row in range(0,len(emdat_record_list)):
        if emdat_record_list[row][3]=='madagascar':
            madagascar.append(emdat_record_list[row])
            madagascar1 = [madagascar[row][10].replace('north','')for row in range(0,len(madagascar))]
            madagascar2 = [madagascar1[row].replace('south','')for row in range(0,len(madagascar1))]
            madagascar3 = [madagascar2[row].replace('east','')for row in range(0,len(madagascar2))]
            madagascar4 = [madagascar3[row].replace('west','')for row in range(0,len(madagascar3))]
            madagascar5 = [madagascar4[row].replace('provinces','')for row in range(0,len(madagascar4))]
            madagascar6 = [madagascar5[row].replace('province','')for row in range(0,len(madagascar5))]
            madagascar7 = [madagascar6[row].replace('mainly','')for row in range(0,len(madagascar6))]
            madagascar8 = [madagascar7[row].replace('districts','')for row in range(0,len(madagascar7))]
            madagascar9 = [madagascar8[row].replace('district','')for row in range(0,len(madagascar8))]
            madagascar10 = [madagascar9[row].replace('communes','')for row in range(0,len(madagascar9))]
    madagascar_clean = list(madagascar)
    for row in range(0,len(madagascar10)):
        madagascar_clean[row][10] = madagascar10[row]
    for row in madagascar_clean:
        emdat_record_clean.append(row)

    malawi = []
    for row in range(0,len(emdat_record_list)):
        if emdat_record_list[row][3]=='malawi':
            malawi.append(emdat_record_list[row])
            malawi1 = [malawi[row][10].replace('district','')for row in range(0,len(malawi))]
    malawi_clean = list(malawi)
    for row in range(0,len(malawi1)):
        malawi_clean[row][10] = malawi1[row]
    for row in malawi_clean:
        emdat_record_clean.append(row)

    mozambique = []
    for row in range(0,len(emdat_record_list)):
        if emdat_record_list[row][3]=='mozambique':
            mozambique.append(emdat_record_list[row])
            mozambique1 = [mozambique[row][10].replace('provinces','')for row in range(0,len(mozambique))]
            mozambique2 = [mozambique1[row].replace('province','')for row in range(0,len(mozambique1))]
            mozambique3 = [mozambique2[row].replace('city','')for row in range(0,len(mozambique2))]
            mozambique4 = [mozambique3[row].replace('districts','')for row in range(0,len(mozambique3))]
            mozambique5 = [mozambique4[row].replace('district','')for row in range(0,len(mozambique4))]
    mozambique_clean = list(mozambique)
    for row in range(0,len(mozambique5)):
        mozambique_clean[row][10] = mozambique5[row]
    for row in mozambique_clean:
        emdat_record_clean.append(row)

    myanmar = []
    for row in range(0,len(emdat_record_list)):
        if emdat_record_list[row][3]=='myanmar':
            myanmar.append(emdat_record_list[row])
            myanmar1 = [myanmar[row][10].replace('north','')for row in range(0,len(myanmar))]
            myanmar2 = [myanmar1[row].replace('west','')for row in range(0,len(myanmar1))]
            myanmar3 = [myanmar2[row].replace('coast','')for row in range(0,len(myanmar2))]
            myanmar4 = [myanmar3[row].replace('division','')for row in range(0,len(myanmar3))]
            myanmar5 = [myanmar4[row].replace('state','')for row in range(0,len(myanmar4))]
    myanmar_clean = list(myanmar)
    for row in range(0,len(myanmar5)):
        myanmar_clean[row][10] = myanmar5[row]
    for row in myanmar_clean:
        emdat_record_clean.append(row)

    nicaragua = []
    for row in range(0,len(emdat_record_list)):
        if emdat_record_list[row][3]=='nicaragua':
            nicaragua.append(emdat_record_list[row])
            nicaragua1 = [nicaragua[row][10].replace('area','')for row in range(0,len(nicaragua))]
            nicaragua2 = [nicaragua1[row].replace('provinces','')for row in range(0,len(nicaragua1))]
            nicaragua3 = [nicaragua2[row].replace('isl.','')for row in range(0,len(nicaragua2))]
            nicaragua4 = [nicaragua3[row].replace('regionautonomadelatlanticonorte','atlanticonorte')for row in range(0,len(nicaragua3))]
            nicaragua5 = [nicaragua4[row].replace('departments','')for row in range(0,len(nicaragua4))]
            nicaragua6 = [nicaragua5[row].replace('department','')for row in range(0,len(nicaragua5))]
            nicaragua7 = [nicaragua6[row].replace('municipalities','')for row in range(0,len(nicaragua6))]
    nicaragua_clean = list(nicaragua)
    for row in range(0,len(nicaragua7)):
        nicaragua_clean[row][10] = nicaragua7[row]
    for row in nicaragua_clean:
        emdat_record_clean.append(row)

    pakistan = []
    for row in range(0,len(emdat_record_list)):
        if emdat_record_list[row][3]=='pakistan':
            pakistan.append(emdat_record_list[row])
            pakistan1 = [pakistan[row][10].replace('level1=','')for row in range(0,len(pakistan))]
            pakistan2 = [pakistan1[row].replace('provinces','')for row in range(0,len(pakistan1))]
    pakistan_clean = list(pakistan)
    for row in range(0,len(pakistan2)):
        pakistan_clean[row][10] = pakistan2[row]
    for row in pakistan_clean:
        emdat_record_clean.append(row)

    peru = []
    for row in range(0,len(emdat_record_list)):
        if emdat_record_list[row][3]=='peru':
            peru.append(emdat_record_list[row])
            peru1 = [peru[row][10].replace('departments','')for row in range(0,len(peru))]
    peru_clean = list(peru)
    for row in range(0,len(peru1)):
        peru_clean[row][10] = peru1[row]
    for row in peru_clean:
        emdat_record_clean.append(row)

    philippines = []
    for row in range(0,len(emdat_record_list)):
        if emdat_record_list[row][3]=='philippines':
            philippines.append(emdat_record_list[row])
            philippines1 = [philippines[row][10].replace('provinces','')for row in range(0,len(philippines))]
            philippines3 = [philippines1[row].replace('municipalities','')for row in range(0,len(philippines1))]
            philippines4 = [philippines3[row].replace('southwetofmanila','manila')for row in range(0,len(philippines3))]
            philippines5 = [philippines4[row].replace('quezonprovince','quezon')for row in range(0,len(philippines4))]
            philippines6 = [philippines5[row].replace('capizprovince','capiz')for row in range(0,len(philippines5))]
            philippines7 = [philippines6[row].replace('includingmanila','manila')for row in range(0,len(philippines6))]
            philippines8 = [philippines7[row].replace('pangasinanprovince','pangasinan')for row in range(0,len(philippines7))]
            philippines9 = [philippines8[row].replace('cebuprovince','cebu')for row in range(0,len(philippines8))]
            philippines10 = [philippines9[row].replace('quirinoprovince','quirino')for row in range(0,len(philippines9))]
            philippines11 = [philippines10[row].replace('tarlacprovince','tarlac')for row in range(0,len(philippines10))]
            philippines12 = [philippines11[row].replace('masbateprovince','masbate')for row in range(0,len(philippines11))]
            philippines13 = [philippines12[row].replace('metromanila','metropolitanmanila')for row in range(0,len(philippines12))]
            philippines14 = [philippines13[row].replace('metromanilamuncipality','metropolitanmanila')for row in range(0,len(philippines13))]
            philippines15 = [philippines14[row].replace('manilacity','manila')for row in range(0,len(philippines14))]
            philippines16 = [philippines15[row].replace('cagayanprov.','cagayan')for row in range(0,len(philippines15))]
            philippines17 = [philippines16[row].replace('cagayanprovince','cagayan')for row in range(0,len(philippines16))]
            philippines18 = [philippines17[row].replace('provincesofcagayan','cagayan')for row in range(0,len(philippines17))]
            philippines19 = [philippines18[row].replace('bilirancity','biliran')for row in range(0,len(philippines18))]
            philippines20 = [philippines19[row].replace('auroraprovince','aurora')for row in range(0,len(philippines19))]
            philippines21 = [philippines20[row].replace('albayprovince','albay')for row in range(0,len(philippines20))]
            philippines22 = [philippines21[row].replace('quirinoregion','quirino')for row in range(0,len(philippines21))]
            philippines23 = [philippines22[row].replace('kalingaprovinces','kalinga')for row in range(0,len(philippines22))]
            philippines24 = [philippines23[row].replace('camarinesnorteprovince','camarinesnorte')for row in range(0,len(philippines23))]
            philippines25 = [philippines24[row].replace('quezoncity','quezon')for row in range(0,len(philippines24))]
            philippines26 = [philippines25[row].replace('launionprovince','launion')for row in range(0,len(philippines25))]
            philippines27 = [philippines26[row].replace('pangasinanprovince','pangasinan')for row in range(0,len(philippines26))]
            philippines28 = [philippines27[row].replace('nuevavizcayaprovince','nuevavizcaya')for row in range(0,len(philippines27))]
            philippines29 = [philippines28[row].replace('isabelaprovince','isabela')for row in range(0,len(philippines28))]
            philippines30 = [philippines29[row].replace('zambalesprovince','zambales')for row in range(0,len(philippines29))]
            philippines31 = [philippines30[row].replace('pampangaprovince','pampanga')for row in range(0,len(philippines30))]
            philippines32 = [philippines31[row].replace('ifugaoprovince','ifugao')for row in range(0,len(philippines31))]
            philippines33 = [philippines32[row].replace('kalingaprovince','kalinga')for row in range(0,len(philippines32))]
            philippines34 = [philippines33[row].replace('benguetprovince','benguet')for row in range(0,len(philippines33))]
            philippines35 = [philippines34[row].replace('ilocosnortemunicipality','ilocosnorte')for row in range(0,len(philippines34))]
            philippines36 = [philippines35[row].replace('rizalmunicipality','rizal')for row in range(0,len(philippines35))]
            philippines37 = [philippines36[row].replace('mandaluyongcity','mandaluyong')for row in range(0,len(philippines36))]
            philippines38 = [philippines37[row].replace('agusandelnorteprovince','agusandelnorte')for row in range(0,len(philippines37))]
            philippines39 = [philippines38[row].replace('muntinlupacity','muntinlupa')for row in range(0,len(philippines38))]
            philippines40 = [philippines39[row].replace('navotascity','navotas')for row in range(0,len(philippines39))]
            philippines41 = [philippines40[row].replace('dinagatisl.','dinagatislands')for row in range(0,len(philippines40))]
            philippines42 = [philippines41[row].replace('northernmindanaoregions','northernmindanao')for row in range(0,len(philippines41))]
            philippines43 = [philippines42[row].replace('mindanaoregions','mindanao')for row in range(0,len(philippines42))]
            philippines44 = [philippines43[row].replace('cordilleraregions','cordillera')for row in range(0,len(philippines43))]
            philippines45 = [philippines44[row].replace('bholaregions','bhola')for row in range(0,len(philippines44))]
    philippines_clean = list(philippines)
    for row in range(0,len(philippines45)):
        philippines_clean[row][10] = philippines45[row]
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='regioni':
                item[n]='regioniilocosregion'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='regionii':
                item[n]='regioniicagayanvalley'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='regioniii':
                item[n]='regioniiicentralluzon'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='regioniv':
                item[n]='regionivsoutherntagalog'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='regioniva':
                item[n]='regionivacalabarzon'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='regionv':
                item[n]='regionvbicolregion'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='regionvi':
                item[n]='regionviwesternvisayas'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='regionvii':
                item[n]='regionviicentralvisayas'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='regionviii':
                item[n]='regionviiieasternvisayas'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='regionix':
                item[n]='regionixzamboangapeninsula'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='regionx':
                item[n]='regionxnorthernmindanao'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='regionxi':
                item[n]='regionxidavaoregion'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='regionxii':
                item[n]='regionxiisoccsksargen'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='regionxiii':
                item[n]='regionxiiicaraga'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='regionsiiv':
                item[n]='regioniilocosregion'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='regionsiii':
                item[n]='regioniiicentralluzon'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='regionsivb':
                item[n]='regionivsoutherntagalog'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='regionivb':
                item[n]='regionivsoutherntagalog'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='regionsiv':
                item[n]='regionivsoutherntagalog'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='regionsi':
                item[n]='regioniilocosregion'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='regionsv':
                item[n]='regionvbicolregion'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='i':
                item[n]='regioniilocosregion'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='reg.i':
                item[n]='regioniilocosregion'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='ii':
                item[n]='regioniicagayanvalley'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='iii':
                item[n]='regioniiicentralluzon'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='reg.iii':
                item[n]='regioniiicentralluzon'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='iva':
                item[n]='regionivacalabarzon'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='iv':
                item[n]='regionivsoutherntagalog'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='reg.iv':
                item[n]='regionivsoutherntagalog'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='v':
                item[n]='regionvbicolregion'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='vi':
                item[n]='regionviwesternvisayas'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='reg.vi':
                item[n]='regionviwesternvisayas'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='vii':
                item[n]='regionviicentralvisayas'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='viii':
                item[n]='regionviiieasternvisayas'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='ix':
                item[n]='regionixzamboangapeninsula'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='x':
                item[n]='regionxnorthernmindanao'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='xi':
                item[n]='regionxidavaoregion'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='xii':
                item[n]='regionxiisoccsksargen'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='xiii':
                item[n]='regionxiiicaraga'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='ilocosregion':
                item[n]='regioniilocosregion'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='cagayanvalley':
                item[n]='regioniicagayanvalley'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='centralluzon':
                item[n]='regioniiicentralluzon'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='calabarzon':
                item[n]='regionivacalabarzon'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='southerntagalog':
                item[n]='regionivsoutherntagalog'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='bicolregion':
                item[n]='regionvbicolregion'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='westernvisayas':
                item[n]='regionviwesternvisayas'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='centralvisayas':
                item[n]='regionviicentralvisayas'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='easternvisayas':
                item[n]='regionviiieasternvisayas'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='zamboangapeninsula':
                item[n]='regionixzamboangapeninsula'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='northernmindanao':
                item[n]='regionxnorthernmindanao'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='davaoregion':
                item[n]='regionxidavaoregion'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='soccsksargen':
                item[n]='regionxiisoccsksargen'
    for item in philippines_clean:
        for n,i in enumerate(item):
            if i=='caraga':
                item[n]='regionxiiicaraga'

    for row in philippines_clean:
        emdat_record_clean.append(row)

    sri_lanka = []
    for row in range(0,len(emdat_record_list)):
        if emdat_record_list[row][3]=='srilanka':
            sri_lanka.append(emdat_record_list[row])
            sri_lanka1 = [sri_lanka[row][10].replace('districts','')for row in range(0,len(sri_lanka))]
    sri_lanka_clean = list(sri_lanka)
    for row in range(0,len(sri_lanka1)):
        sri_lanka_clean[row][10] = sri_lanka1[row]
    for row in sri_lanka_clean:
        emdat_record_clean.append(row)

    tajikistan = []
    for row in range(0,len(emdat_record_list)):
        if emdat_record_list[row][3]=='tajikistan':
            tajikistan.append(emdat_record_list[row])
            tajikistan1 = [tajikistan[row][10].replace('leninabadregion','leninabad')for row in range(0,len(tajikistan))]
    tajikistan_clean = list(tajikistan)
    for row in range(0,len(tajikistan1)):
        tajikistan_clean[row][10] = tajikistan1[row]
    for row in tajikistan_clean:
        emdat_record_clean.append(row)

    zimbabwe = []
    for row in range(0,len(emdat_record_list)):
        if emdat_record_list[row][3]=='zimbabwe':
            zimbabwe.append(emdat_record_list[row])
            zimbabwe1 = [zimbabwe[row][10].replace('districts','')for row in range(0,len(zimbabwe))]
            zimbabwe2 = [zimbabwe1[row].replace('province','')for row in range(0,len(zimbabwe1))]
    zimbabwe_clean = list(zimbabwe)
    for row in range(0,len(zimbabwe2)):
        zimbabwe_clean[row][10] = zimbabwe2[row]
    for row in zimbabwe_clean:
        emdat_record_clean.append(row)

    #append the data that don't need corrections
    bhutan = []
    for row in range(0,len(emdat_record_list)):
         if emdat_record_list[row][3]=='bhutan':
             bhutan.append(emdat_record_list[row])
    for row in bhutan:
        emdat_record_clean.append(row)

    cambodia = []
    for row in range(0,len(emdat_record_list)):
         if emdat_record_list[row][3]=='cambodia':
             cambodia.append(emdat_record_list[row])
    for row in cambodia:
        emdat_record_clean.append(row)

    somalia = []
    for row in range(0,len(emdat_record_list)):
         if emdat_record_list[row][3]=='somalia':
             somalia.append(emdat_record_list[row])
    for row in somalia:
        emdat_record_clean.append(row)

    swaziland = []
    for row in range(0,len(emdat_record_list)):
         if emdat_record_list[row][3]=='swaziland':
             swaziland.append(emdat_record_list[row])
    for row in swaziland:
        emdat_record_clean.append(row)

    tanzania = []
    for row in range(0,len(emdat_record_list)):
         if emdat_record_list[row][3]=='tanzania':
             tanzania.append(emdat_record_list[row])
    for row in tanzania:
        emdat_record_clean.append(row)

    emdat_record_clean_out = [[x.replace(' ','') for x in l] for l in emdat_record_clean]

    return emdat_record_clean_out





