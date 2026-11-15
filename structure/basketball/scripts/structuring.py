"""US Basketball universe: structuring 2022/23 -> summer 2026. Seeded, re-runnable."""
import json, math, random
R = random.Random(20230218)  # announcement day, All-Star Saturday, Salt Lake City
out = {}

def roll(p): return R.random() < p
def pick(opts):
    tot = sum(w for _, w in opts); x = R.random() * tot
    for o, w in opts:
        x -= w
        if x <= 0: return o
    return opts[-1][0]

# ---------- 2022/23: CBA ----------
# Art. 56: the union's agreement is negotiated in the April 2023 CBA; the roll is the timing of the last draft
out['last_draft'] = pick([(2026,3),(2027,1)])

# ---------- NBA clubs: owner investment tier (3 high .. 1 lower), metro talent pull (1-3), region ----------
NBA = {
 'Atlanta Hawks':(2,3,'E'),'Boston Celtics':(2,2,'E'),'Brooklyn Nets':(3,3,'E'),'Charlotte Hornets':(1,2,'E'),
 'Chicago Bulls':(2,3,'E'),'Cleveland Cavaliers':(3,2,'E'),'Detroit Pistons':(3,2,'E'),'Indiana Pacers':(2,2,'E'),
 'Miami Heat':(3,3,'E'),'Milwaukee Bucks':(2,1,'E'),'New York Knicks':(3,3,'E'),'Orlando Magic':(2,3,'E'),
 'Philadelphia 76ers':(3,3,'E'),'Toronto Raptors':(3,2,'E'),'Washington Wizards':(2,3,'E'),
 'Dallas Mavericks':(3,3,'W'),'Denver Nuggets':(3,1,'W'),'Golden State Warriors':(3,2,'W'),'Houston Rockets':(3,3,'W'),
 'Los Angeles Clippers':(3,3,'W'),'Los Angeles Lakers':(3,3,'W'),'Memphis Grizzlies':(1,2,'W'),'Minnesota Timberwolves':(1,1,'W'),
 'New Orleans Pelicans':(1,2,'W'),'Oklahoma City Thunder':(2,1,'W'),'Phoenix Suns':(3,2,'W'),'Portland Trail Blazers':(1,1,'W'),
 'Sacramento Kings':(2,2,'W'),'San Antonio Spurs':(2,2,'W'),'Utah Jazz':(3,1,'W'),
}

# ---------- G League 2022/23 (30 clubs) ----------
# club: (parent or None, ownership, arena 2022/23, capacity, near_parent)
G = {
 'Austin Spurs':('San Antonio Spurs','parent','H-E-B Center at Cedar Park',7200,False),
 'Birmingham Squadron':('New Orleans Pelicans','parent','Legacy Arena',17000,False),
 'Capital City Go-Go':('Washington Wizards','parent','Entertainment and Sports Arena',4200,True),
 'Cleveland Charge':('Cleveland Cavaliers','parent','Wolstein Center',13000,True),
 'College Park Skyhawks':('Atlanta Hawks','parent','Gateway Center Arena',3500,True),
 'Delaware Blue Coats':('Philadelphia 76ers','parent','Chase Fieldhouse',2500,False),
 'Fort Wayne Mad Ants':('Indiana Pacers','parent','Memorial Coliseum',10500,False),
 'G League Ignite':(None,'league','Dollar Loan Center',6000,False),
 'Grand Rapids Gold':('Denver Nuggets','hybrid','DeltaPlex Arena',4500,False),
 'Greensboro Swarm':('Charlotte Hornets','parent','Novant Health Fieldhouse',2500,False),
 'Iowa Wolves':('Minnesota Timberwolves','parent','Wells Fargo Arena',16110,False),
 'Lakeland Magic':('Orlando Magic','parent','RP Funding Center',8000,False),
 'Long Island Nets':('Brooklyn Nets','parent','Nassau Coliseum',13500,True),
 'Maine Celtics':('Boston Celtics','parent','Portland Exposition Building',3100,False),
 'Memphis Hustle':('Memphis Grizzlies','parent','Landers Center',8362,True),
 'Mexico City Capitanes':(None,'independent','Arena CDMX',22300,False),
 'Motor City Cruise':('Detroit Pistons','parent','Wayne State Fieldhouse',3000,True),
 'Oklahoma City Blue':('Oklahoma City Thunder','parent','Paycom Center',18203,True),
 'Ontario Clippers':('Los Angeles Clippers','parent','Toyota Arena',10832,False),
 'Raptors 905':('Toronto Raptors','parent','Paramount Fine Foods Centre',5000,True),
 'Rio Grande Valley Vipers':('Houston Rockets','hybrid','Bert Ogden Arena',9000,False),
 'Salt Lake City Stars':('Utah Jazz','parent','Maverik Center',12500,True),
 'Santa Cruz Warriors':('Golden State Warriors','parent','Kaiser Permanente Arena',2505,False),
 'Sioux Falls Skyforce':('Miami Heat','parent','Sanford Pentagon',3250,False),
 'South Bay Lakers':('Los Angeles Lakers','parent','UCLA Health Training Center',750,True),
 'Stockton Kings':('Sacramento Kings','parent','Stockton Arena',10117,False),
 'Texas Legends':('Dallas Mavericks','hybrid','Comerica Center',4500,True),
 'Westchester Knicks':('New York Knicks','parent','Westchester County Center',5000,True),
 'Windy City Bulls':('Chicago Bulls','parent','Now Arena',10000,True),
 'Wisconsin Herd':('Milwaukee Bucks','parent','Oshkosh Arena',3500,False),
}
aff = {}
for c,(par,own,ar,cap,near) in G.items():
    if own == 'hybrid':
        indep = roll(0.55)
        aff[c] = {'choice':'independent' if indep else 'affiliate','parent':None if indep else par,'former':par}
    elif own == 'league': aff[c] = {'choice':'folds after 2023/24','parent':None}
    elif own == 'independent': aff[c] = {'choice':'independent','parent':None}
    else: aff[c] = {'choice':'affiliate','parent':par}
out['affiliation'] = aff

parents_with = {v['parent'] for v in aff.values() if v.get('parent')}
without = [n for n in NBA if n not in parents_with]
# Ignite's slot: the Board lets one NBA club without an affiliate found one for 2024/25
w = {'Portland Trail Blazers':3,'Phoenix Suns':3}
cand = [(n, w.get(n,2)) for n in without]
slot = pick(cand)
NEWAFF = {'Portland Trail Blazers':('Rip City Remix','Chiles Center',4852,False),
          'Phoenix Suns':('Valley Suns','Mullett Arena',5000,True),
          'Denver Nuggets':('Denver Gold','Ball Arena (lower bowl)',8000,True),
          'Houston Rockets':('Houston Vipers','Toyota Center (lower bowl)',8000,True),
          'Dallas Mavericks':('Dallas Legends','American Airlines Center (lower bowl)',8000,True)}
out['ignite_slot'] = {'club':slot,'new':NEWAFF[slot][0]}
out['nba_without_affiliate_2026'] = [n for n in without if n != slot]

# ---------- Venues: G League licence needs 4,000 (licensing round 2024/25) ----------
VENUE_OPTS = {
 'College Park Skyhawks':[('McCamish Pavilion, Georgia Tech (8,600)',3),('State Farm Arena (16,600)',2),('Gateway Center expanded to 4,000',2)],
 'Delaware Blue Coats':[('Bob Carpenter Center, Newark (5,000)',4),('Wells Fargo Center, Philadelphia (20,000)',2)],
 'Greensboro Swarm':[('Greensboro Coliseum main arena (22,000), next door',6),('Fieldhouse expanded to 4,000',1)],
 'Maine Celtics':[('Cross Insurance Arena, Portland (6,733)',6),('TD Garden (19,580)',1)],
 'Motor City Cruise':[('Calihan Hall, Detroit Mercy (8,295)',3),('Little Caesars Arena (20,332)',3)],
 'Santa Cruz Warriors':[('Kaiser Permanente Arena expanded to 4,000 (temporary stands, then permanent)',3),('Provident Credit Union Event Center, San Jose State (5,000)',3),('Chase Center (18,064)',1)],
 'Sioux Falls Skyforce':[('Sanford Premier Center, Sioux Falls (12,000)',7)],
 'South Bay Lakers':[('move to Acrisure Arena, Thousand Palms, as the Coachella Valley Lakers (11,000)',4),('Walter Pyramid, Long Beach (4,200)',3),('Crypto.com Arena (18,997)',2)],
 'Wisconsin Herd':[('Resch Center, Green Bay (8,600)',3),('Oshkosh Arena expanded to 4,000',3),('Fiserv Forum (17,341)',1)],
}
ven = {}
for c,o in VENUE_OPTS.items(): ven[c] = pick(o)
# Mad Ants: Pacers' Noblesville plan must reach 4,000
ven['Fort Wayne Mad Ants'] = pick([('Noblesville arena redesigned to 4,200, opens 2025 as the Noblesville Boom',5),('stay at Memorial Coliseum, Fort Wayne (10,500)',3)])
out['venues'] = ven

# ---------- Academy facilities (seniors use the one practice court) ----------
fac = {}
for n,(inv,pull,reg) in NBA.items():
    if n == 'Los Angeles Clippers':
        s = 'keeps the old Playa Vista training centre (2 courts) for the academy, builds a 4-court academy centre in Inglewood'
        opens = pick([('2025',4),('2026',3),('2027',1)]); fac[n]={'plan':s,'opens':opens}; continue
    pb = {3:0.85,2:0.6,1:0.4}[inv]
    if roll(pb):
        courts = pick([(3,2),(4,4),(6,2 if inv==3 else 1)])
        opens = pick([('2025',3 if inv==3 else 2),('2026',4),('2027',2)])
        fac[n] = {'plan':f'new {courts}-court academy centre','opens':opens}
    else:
        fac[n] = {'plan':pick([('university gyms rented',3),('high school gyms rented',3),('community centre partnership',2)]),'opens':None}
out['facilities'] = fac

# ---------- Academy grades 2024/25 ----------
def grade(score):
    return 'Platinum' if score >= 8.6 else ('Gold' if score >= 6.6 else 'Silver')
grades = {}
for n,(inv,pull,reg) in NBA.items():
    f = fac[n]; fs = 3 if (f['opens']=='2025') else (2.2 if f['opens'] else 1.2)
    sc = fs + 0.7*inv + R.gauss(2.5,0.6) + R.gauss(1.6,0.5)  # facilities + investment + coaching/medical + education
    grades[n] = {'grade':grade(sc),'score':round(sc,2)}
# G League academies: own academy, shares parent's centre if near
for c,(par,own,ar,cap,near) in G.items():
    if aff[c]['choice'].startswith('folds'): continue
    p = aff[c].get('parent')
    if p and near and fac[p]['opens']=='2025': fs = 2.4
    elif p and near and fac[p]['opens']: fs = 1.8
    else: fs = 1.0
    inv = NBA[p][0] if p else 1
    sc = fs + 0.6*inv + R.gauss(2.2,0.6) + R.gauss(1.4,0.5)
    grades[c] = {'grade':grade(sc),'score':round(sc,2)}
nc = NEWAFF[slot][0]
grades[nc] = {'grade':grade(1.0+0.6*NBA[slot][0]+R.gauss(2.2,0.6)+R.gauss(1.4,0.5))}
out['grades'] = grades

# ---------- AAND: new clubs and existing ones (licence round 2024/25) ----------
NEWCLUBS = [  # name, region, arena, p(applies and is licensed)
 ('Seattle Basketball Club','W','Climate Pledge Arena',0.85),('Las Vegas Basketball Club','W','Dollar Loan Center, Henderson',0.8),
 ('San Diego Basketball Club','W','Pechanga Arena',0.5),('Anaheim Basketball Club','W','Honda Center',0.3),
 ('Kansas City Basketball Club','M','T-Mobile Center',0.6),('St. Louis Basketball Club','M','Enterprise Center',0.5),
 ('Cincinnati Basketball Club','M','Heritage Bank Center',0.4),('Columbus Basketball Club','M','Nationwide Arena',0.35),('Omaha Basketball Club','M','CHI Health Center',0.3),
 ('Pittsburgh Basketball Club','E','PPG Paints Arena',0.45),('Baltimore Basketball Club','E','CFG Bank Arena',0.4),
 ('Hartford Basketball Club','E','XL Center',0.35),('Buffalo Basketball Club','E','KeyBank Center',0.3),('Providence Basketball Club','E','Amica Mutual Pavilion',0.25),
 ('Louisville Basketball Club','S','KFC Yum! Center',0.55),('Nashville Basketball Club','S','Bridgestone Arena',0.55),
 ('Austin Basketball Club','S','Moody Center',0.5),('Tampa Bay Basketball Club','S','Amalie Arena',0.45),('Raleigh Basketball Club','S','Lenovo Center',0.3),('Jacksonville Basketball Club','S','VyStar Veterans Memorial Arena',0.25),
]
aand_ind = []
for nm,reg,ar,p in NEWCLUBS:
    if roll(p): aand_ind.append({'club':nm,'region':reg,'arena':ar,'str':round(R.gauss(78,4.5),1),'founded':pick([('2023',3),('2024',2)])})
# Overtime Elite: needs 1,500 seats (OTE Arena seats 1,200)
ote = roll(0.7)
if ote:
    aand_ind.append({'club':'Overtime Elite','region':'S','arena':pick([('OTE Arena expanded to 1,600',3),('Gateway Center Arena, College Park (3,500)',2)]),'str':round(R.gauss(70,3),1),'founded':'2021'})
out['ote_licensed'] = ote
# TBL clubs: semi-professional; licence chance small
TBL = [('St. Louis Griffins','M'),('Albany Patroons','E'),('Kansas City Defenders','M'),('Tampa Bay Titans','S'),('Dallas Stampede','S'),('Raleigh Firebirds','S')]
tbl_lic = [ {'club':c,'region':r,'arena':'—','str':round(R.gauss(62,3),1),'founded':'TBL'} for c,r in TBL if roll(0.12)]
aand_ind += tbl_lic
out['aand_independents'] = aand_ind

# ---------- University round, spring 2026 ----------
# name, region, strength (programme, narrator), class
U = """Gonzaga W 88 mm|UCLA W 84 bb|USC W 76 p|Arizona W 87 p|Arizona State W 70 p|Oregon W 78 p|Washington W 70 p|Utah W 68 p|Colorado W 69 p|BYU W 82 p|Utah State W 75 mm|San Diego State W 80 mm|Saint Mary's W 80 mm|New Mexico W 74 m|UNLV W 70 m|Nevada W 72 m|Boise State W 75 m|Colorado State W 74 m|Fresno State W 58 m|San Jose State W 55 m|Stanford W 70 p|California W 66 p|Washington State W 66 m|Oregon State W 64 m|Santa Clara W 70 m|San Francisco W 70 m|Loyola Marymount W 62 m|Pepperdine W 55 l|Long Beach State W 58 m|UC Irvine W 72 m|UC San Diego W 70 m|UC Santa Barbara W 66 m|Cal State Fullerton W 52 l|Cal State Northridge W 60 l|Grand Canyon W 74 m|Wyoming W 60 m|Montana W 56 l|Hawaii W 55 l|Seattle U W 58 l|UC Riverside W 58 l|UC Davis W 55 l|Cal Baptist W 57 l|Northern Arizona W 50 l|Weber State W 52 l
Michigan M 90 p|Michigan State M 85 p|Purdue M 86 p|Illinois M 86 p|Indiana M 75 bb|Ohio State M 76 p|Wisconsin M 82 p|Iowa M 76 p|Iowa State M 85 p|Kansas M 86 bb|Kansas State M 72 p|Nebraska M 76 p|Minnesota M 66 p|Northwestern M 72 p|Notre Dame M 66 p|Marquette M 80 be|Creighton M 79 be|Xavier M 76 be|Butler M 72 be|DePaul M 60 be|Cincinnati M 76 p|Dayton M 74 mm|Missouri M 74 p|Saint Louis M 72 m|Drake M 72 m|Bradley M 68 m|Loyola Chicago M 66 m|Wichita State M 68 m|Akron M 66 m|Northern Iowa M 64 m|Illinois State M 60 l|Kent State M 58 l|Ohio M 58 l|Oakland M 60 l|Toledo M 58 l
UConn E 90 be|Duke E 92 bb|North Carolina E 84 bb|Villanova E 76 be|St. John's E 84 be|Georgetown E 66 be|Providence E 70 be|Seton Hall E 66 be|Syracuse E 70 p|Pittsburgh E 70 p|Boston College E 58 p|Penn State E 68 p|Rutgers E 70 p|Maryland E 80 p|Virginia E 76 p|Virginia Tech E 68 p|NC State E 74 p|Wake Forest E 72 p|West Virginia E 74 p|VCU E 76 mm|George Mason E 70 m|Richmond E 60 m|Saint Joseph's E 68 m|Temple E 62 m|Princeton E 64 m|Yale E 70 m|Harvard E 58 l|Drexel E 58 l|Hofstra E 60 l|Iona E 60 l|St. Bonaventure E 64 m|UMass E 58 m|Rhode Island E 60 m|Davidson E 62 m|Duquesne E 60 m|George Washington E 62 m|Towson E 56 l
Kentucky S 84 bb|Tennessee S 88 p|Alabama S 86 p|Auburn S 87 p|Florida S 89 p|Arkansas S 82 p|LSU S 70 p|Ole Miss S 76 p|Mississippi State S 76 p|Texas S 78 p|Texas A&M S 79 p|Texas Tech S 85 p|Houston S 91 mm|Baylor S 80 p|TCU S 72 p|Oklahoma S 70 p|Oklahoma State S 66 p|Georgia S 74 p|South Carolina S 66 p|Vanderbilt S 76 p|Memphis S 76 mm|Florida State S 66 p|Miami S 66 p|Clemson S 78 p|Georgia Tech S 62 p|Louisville S 80 p|UCF S 70 p|SMU S 72 p|Florida Atlantic S 72 m|Tulane S 60 m|Belmont S 66 m|Murray State S 62 m|Liberty S 70 m|McNeese S 70 m|Charleston S 66 m|UAB S 68 m|North Texas S 70 m|UTEP S 56 l|Chattanooga S 56 l|Western Kentucky S 60 m|Furman S 64 m|High Point S 70 m|Samford S 62 l|App State S 60 l|Troy S 60 l"""
APPLY = {'bb':0.40,'be':0.60,'mm':0.65,'p':0.42,'m':0.35,'l':0.28}
LIC = {'bb':0.95,'be':0.9,'mm':0.85,'p':0.9,'m':0.6,'l':0.35}
unis = []
for line in U.split('\n'):
    for it in line.split('|'):
        parts = it.rsplit(' ',3); nm, reg, st, cl = parts[0], parts[1], int(parts[2]), parts[3]
        a = roll(APPLY[cl]); lic = a and roll(LIC[cl])
        unis.append({'club':nm,'region':reg,'str':st+round(R.gauss(0,2.5),1),'class':cl,'applied':a,'aand_licence':lic})
out['others_applied'] = sum(1 for _ in range(250) if roll(0.18))  # remaining D1, D2, NAIA programmes; all SD1
# Placement: 16 per conference, best by strength among licensed (independents + universities)
conf = {}
REGN = {'W':'West','M':'Midwest','E':'East','S':'South'}
for rg in 'WMES':
    pool = [dict(x, kind='new club') for x in aand_ind if x['region']==rg] + [dict(x, kind='university') for x in unis if x['region']==rg and x['aand_licence']]
    pool.sort(key=lambda x:-x['str'])
    conf[REGN[rg]] = {'in':pool[:16],'to_sd1':pool[16:]}
# fill a short conference from the nearest leftover
for rg,nb in [('West','Midwest'),('Midwest','South'),('East','Midwest'),('South','Midwest')]:
    while len(conf[rg]['in']) < 16 and conf[nb]['to_sd1']:
        conf[rg]['in'].append(dict(conf[nb]['to_sd1'].pop(0), moved_from=nb))
out['aand'] = conf
out['universities'] = unis

# ---------- 2025/26 first youth season (narrator levels, football bases carry over) ----------
BASE = {12:30,13:33,14:37,15:41,16:44,17:47,18:50,19:52}
def team_level(age, tier, pull, grd, inv):
    bonus = {'NBA':14,'G':10,'AAND':6}[tier]
    gb = {'Platinum':1.5,'Gold':0.7,'Silver':0}[grd]
    first_year = -1.5 if age >= 16 else 0  # older squads assembled in one summer
    return BASE[age] + bonus + 0.9*(pull-2) + gb + 0.4*(inv-2) + first_year + R.gauss(0,1.6)
def game(a,b):  # margin model: 1.6 points per level point + 2 home, sd 11
    m = 1.6*(a-b) + 2 + R.gauss(0,11)
    return m > 0
def league(teams, rr):  # teams: name->level ; rr: 1 single, 2 double
    w = {t:0 for t in teams}; names = list(teams)
    for i,a in enumerate(names):
        for b in names[i+1:]:
            legs = [(a,b),(b,a)] if rr==2 else [((a,b) if roll(0.5) else (b,a))]
            for h,v in legs:
                if game(teams[h],teams[v]): w[h]+=1
                else: w[v]+=1
    return sorted(w.items(), key=lambda x:-x[1])
def playoff(seeds, lv):
    while len(seeds) > 1:
        nxt=[]
        for i in range(len(seeds)//2):
            a,b = seeds[i], seeds[-1-i]
            nxt.append(a if game(lv[a],lv[b]) else b)
        seeds = nxt
    return seeds[0]
youth = {}
nba_e = [n for n in NBA if NBA[n][2]=='E']; nba_w=[n for n in NBA if NBA[n][2]=='W']
g_clubs = [c for c in G if not aff[c]['choice'].startswith('folds')] + [nc]
WEST_G = {'Austin Spurs','Birmingham Squadron','Grand Rapids Gold','Iowa Wolves','Memphis Hustle','Mexico City Capitanes','Oklahoma City Blue','Ontario Clippers','Rio Grande Valley Vipers','Salt Lake City Stars','Santa Cruz Warriors','Sioux Falls Skyforce','South Bay Lakers','Stockton Kings','Texas Legends','Rip City Remix','Valley Suns'}
def gpull(c):
    p = aff[c].get('parent') if c in aff else slot
    base = {'Mexico City Capitanes':1,'Grand Rapids Gold':1,'Rio Grande Valley Vipers':2,'Texas Legends':3}.get(c)
    if base: return base, 1
    return max(1, NBA[p][1] - (0 if G.get(c,(0,0,0,0,True))[4] else 1)), NBA[p][0]
for age in range(12,20):
    rr = 1 if age <= 14 else 2
    res = {}
    lv = {n: team_level(age,'NBA',NBA[n][1],grades[n]['grade'],NBA[n][0]) for n in NBA}
    st_e = league({n:lv[n] for n in nba_e}, rr); st_w = league({n:lv[n] for n in nba_w}, rr)
    four = [st_e[0][0], st_w[0][0], st_e[1][0], st_w[1][0]]
    res['NBA'] = {'east':st_e,'west':st_w,'champion':playoff(four, lv),'levels':{k:round(v,1) for k,v in lv.items()}}
    lg = {}
    for c in g_clubs:
        pl, inv = gpull(c); lg[c] = team_level(age,'G',pl,grades[c]['grade'],inv)
    ge = {c:lg[c] for c in g_clubs if c not in WEST_G}; gw = {c:lg[c] for c in g_clubs if c in WEST_G}
    s_e = league(ge, rr); s_w = league(gw, rr)
    res['G'] = {'east':s_e,'west':s_w,'champion':playoff([s_e[0][0], s_w[0][0], s_e[1][0], s_w[1][0]], lg),'levels':{k:round(v,1) for k,v in lg.items()}}
    la = {x['club']: team_level(age,'AAND',2,'Silver',2) for x in aand_ind}
    s_a = league(la, rr) if len(la) > 1 else []
    res['AAND'] = {'table':s_a,'levels':{k:round(v,1) for k,v in la.items()}}
    if age >= 14:  # National Basketball Youth Cup: AAND first, then G League, then NBA (64-team bracket by draw)
        alllv = {**{('NBA',k):v for k,v in lv.items()}, **{('G',k):v for k,v in lg.items()}, **{('AAND',k):v for k,v in la.items()}}
        def ko(lst):
            R.shuffle(lst); nxt=[]
            if len(lst)%2: nxt.append(lst.pop())
            nxt += [a if game(alllv[a],alllv[b]) else b for a,b in zip(lst[::2],lst[1::2])]
            return nxt
        alive = [k for k in alllv if k[0]=='AAND']
        while len(alive) > 2: alive = ko(alive)
        alive += [k for k in alllv if k[0]=='G']
        while len(alive) > 16: alive = ko(alive)
        alive += [k for k in alllv if k[0]=='NBA']
        while len(alive) > 1: alive = ko(alive)
        res['cup'] = alive[0]
    youth[f'U{age}'] = res
out['youth'] = youth
json.dump(out, open('structuring.json','w'), indent=1, default=str)
print('last draft:', out['last_draft'])
print('affiliation:', {k:v['choice'] for k,v in aff.items() if k in ('Grand Rapids Gold','Rio Grande Valley Vipers','Texas Legends')})
print('ignite slot:', out['ignite_slot'], 'without:', out['nba_without_affiliate_2026'])
print('venues:', json.dumps(ven, indent=0))
print('fac:', json.dumps(fac, indent=0))
print('grades:', {k:v['grade'] for k,v in grades.items()})
print('aand ind:', [(x['club'],x['region'],x['str']) for x in aand_ind])
for k,v in conf.items(): print(k, [(x['club'],x['str']) for x in v['in']], '| to SD1:', [x['club'] for x in v['to_sd1']])
print('applied unis:', sum(u['applied'] for u in unis), 'licensed', sum(u['aand_licence'] for u in unis), 'others', out['others_applied'])
print('not applied:', [u['club'] for u in unis if not u['applied']])
for a,r in youth.items(): print(a, 'NBA', r['NBA']['champion'], '| G', r['G']['champion'], '| AAND', r['AAND']['table'][:1], '| cup', r.get('cup'))

# ---------- Fixes after first run (same seed stream continues) ----------
# Supplementary round, May 2026: places left after the main round
licensed = [x for x in aand_ind] + [u for u in unis if u['aand_licence']]
left = 64 - len(licensed)
supp = []
for u in unis:
    if not u['applied'] and u['class'] in ('bb','be','mm','p') and roll(0.3):
        if roll(LIC[u['class']]): supp.append(u)
supp.sort(key=lambda x:-x['str'])
out['supp_applicants'] = [(u['club'],u['region'],u['str']) for u in supp]
out['supp_in'] = [u['club'] for u in supp[:left]]
print('left', left, 'supp applicants', out['supp_applicants'], 'in', out['supp_in'])
json.dump(out, open('structuring.json','w'), indent=1, default=str)

# ---------- Reasons for failed AAND licences, California SD1 ----------
fails = {}
for u in unis:
    if u['applied'] and not u['aand_licence']:
        fails[u['club']] = pick([('no proof of national travel funding',3),('partner academies for U12-U16 not in place',3),('basketball income too small for the 70% wage rule',2),('debt above the limit',1)])
out['licence_fails'] = fails
CA_CAND = [('Cal Poly',58),('Cal State Bakersfield',50),('Pacific',48),('Sacramento State',50),('Cal State Dominguez Hills',47),('Cal State LA',46),('Cal Poly Pomona',48),('Chico State',45),('Point Loma',46),('Westmont',47),('Biola',43),('Cal State San Bernardino',45),('Concordia Irvine',44),('Cal State San Marcos',44),('Stanislaus State',41),('Cal State East Bay',41)]
ca_sd1 = [("Saint Mary's",85.0),('UC Riverside',61.5)]
for n,s in CA_CAND:
    if roll(0.55): ca_sd1.append((n, s+round(R.gauss(0,2),1)))
out['ca_sd1'] = ca_sd1
print('fails', fails); print('CA SD1', len(ca_sd1), ca_sd1)
json.dump(out, open('structuring.json','w'), indent=1, default=str)
# California SD1 needs 12-16: community colleges also applied in the state round (Art. 57: any university or college)
CCC = [('El Camino College',44),('Long Beach City College',45),('Ventura College',43),('Fresno City College',44),('City College of San Francisco',43),('Cerritos College',42),('Riverside City College',43),('Santa Rosa Junior College',41)]
cc_app = [(n, s+round(R.gauss(0,2),1)) for n,s in CCC if roll(0.35)]
cc_app.sort(key=lambda x:-x[1])
need = max(0, 12 - len(ca_sd1))
out['ca_cc_applied'] = cc_app; out['ca_sd1'] = ca_sd1 + cc_app[:need]; out['ca_sd2_from_cc'] = cc_app[need:]
print('CC', cc_app, 'SD1 final', len(out['ca_sd1']))
json.dump(out, open('structuring.json','w'), indent=1, default=str)
out['clippers_centre_month'] = pick([('September 2026',3),('October 2026',3),('December 2026',2),('February 2027',1)])
for c in ['Los Angeles Lakers','Los Angeles Clippers']: pass
json.dump(out, open('structuring.json','w'), indent=1, default=str)
print('clip month', out['clippers_centre_month'])
# California SD1, last two places: adult clubs (user decision). Real California semi-pro clubs, strength rolled
ADULT = [('San Diego Sharks',52,'Canyon Crest Academy, San Diego (2,900)'),('Bakersfield Majestics',51,'Bakersfield College'),('San Diego Surf',47,'HourGlass Arena, Miramar College')]
ad = sorted([(n, s+round(R.gauss(0,2.5),1), v) for n,s,v in ADULT if roll(0.85)], key=lambda x:-x[1])
out['ca_adult_applied'] = ad; out['ca_sd1_adult'] = ad[:2]
print('adult', ad)
json.dump(out, open('structuring.json','w'), indent=1, default=str)
