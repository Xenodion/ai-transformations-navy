> **BROUILLON HISTORIQUE NON VÉRIFIÉ — NE PAS CITER COMME SOURCE.** Les chiffres, diagnostics, benchmarks et choix de portefeuille ci-dessous doivent être audités avant toute reprise. Voir `work/roadmap.md` et `sources/register.md`.

# Plan Directeur de Transformation IA — TotalEnergies SE
## Dossier Complet de Cadrage Stratégique, Modélisation & Comex Memo

> **Équipe projet :** Alexandre Waerniers, Vincent Lamy, Yoni Mahieddine, Nahel Bachriri  
> **Entreprise cible :** TotalEnergies SE (Ticker : TTE, Siège : Tour Coupole, Courbevoie)  
> **Échéance :** Soutenance du 16 Novembre 2026 (15 min pitch + 5 min Q&A)  
> **Rôle du jury :** Le professeur incarne le Président-Directeur Général (Patrick Pouyanné) sous un questionnement sceptique.

---

## Guide Méthodologique & Traçabilité des Données

Afin de répondre aux exigences de rigueur du Comex et aux consignes académiques, **chaque donnée chiffrée** de ce document est rigoureusement typée selon la nomenclature suivante :
* **`[URD TotalEnergies]` :** Donnée officielle certifiée issue du Document d'Enregistrement Universel (URD 2023/2024) ou des résultats financiers et opérationnels officiels (FY 2024 & T3 2025).
* **`[Benchmark Sectoriel - Auteur]` :** Ratio de marché ou métrique industrielle reconnue (McKinsey Energy Insights, Wood Mackenzie, Gartner, BCG, IEA).
* **`[Hypothèse Cadrée]` :** Estimation interne modélisée pour l'exercice, dont le mode de calcul et les variables sous-jacentes sont explicitement exposés pour être auditables par un directeur financier.

---

## PARTIE I : LE COMEX MEMO (2 PAGES EXÉCUTIVES)

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                         PAGE 1                                         │
│                                                                                        │
│ 1. THESIS (L'ARBITRAGE ET LA DÉCISION)                                                 │
│    Décision demandée : Approuver une enveloppe d'investissement IA de 195 M€ sur 3 ans│
│    (dont Tranche 1 ferme de 65 M€ débloquée ce jour), pour franchir le bottleneck      │
│    des données industrielles OT/IT et générer 142 M€ d'EBIT récurrent annuel à M36.    │
│    Contexte : Maintien du point mort amont pétrolier < 30 $/b [URD], passage à l'échelle│
│    de l'Integrated Power (34 GW renouvelables [URD], objectif ROACE ~12%) et mise en   │
│    conformité obligatoire EU AI Act (Annexe III - Infrastructures énergétiques).       │
│                                                                                        │
│ 2. PORTFOLIO MIX (THREE HORIZONS & VALUE LEVERS)                                       │
│    Allocation stratégique 65% H1 / 25% H2 / 10% H3 (déviation volontaire du 70-20-10   │
│    pour accélérer la flexibilité et le trading sur l'électricité intégrée).            │
│    - H1 Core Optimization (65%) : 4 cas d'usage (Raffinage, E&P, Retail, Copilot)     │
│    - H2 Adjacent Growth (25%) : 4 cas d'usage (PowerFlow, LNG Bunker, Méthane, Chimie)│
│    - H3 Transformational (10%) : 3 cas d'usage (GeoMol SAF, Séquestration CO2, VPP)   │
│                                                                                        │
│ 3. ENVELOPE & BALANCE CAPEX / OPEX (TRAJECTOIRE 3 & 5 ANS)                             │
│    Enveloppe 3 ans ferme : 195 M€  │  Trajectoire 5 ans consolidée : 288 M€           │
│    - CAPEX (3 ans) : 85 M€ (43.6%) — HPC Pangea 5 (30 M€), Data Fabric OT (40 M€),    │
│      capteurs IoT AUSEA (15 M€) capitalisables selon IFRS / IAS 38.                    │
│    - OPEX (3 ans) : 110 M€ (56.4%) — Cloud burst Azure/AWS & inférence (25 M€),       │
│      licences SaaS industrielles (25 M€), Talents & FDE (35 M€), Change & CSE (25 M€). │
│                                                                                        │
│ 4. SCENARIOS & PROBABILITÉS EXPLICITES (VALEUR ESPÉRÉE - EV)                           │
│    - Downside (20%) : Retard adoption terrain, friction OT -> ENPV -18.2 M€ (Loss Cap) │
│    - Base Case (60%) : Déploiement nominal 5 branches -> ENPV +68.2 M€ @ 11% à 3 ans  │
│    - Upside (20%) : Surperformance trading électricité & e-fuels -> ENPV +135.4 M€    │
│    -> ENPV Pondérée (EV) : +64.4 M€ à 3 ans (et +161.8 M€ à 5 ans).                    │
└────────────────────────────────────────────────────────────────────────────────────────┘
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                         PAGE 2                                         │
│                                                                                        │
│ 5. FINANCIAL ANALYSIS (CLEARANCE DU HURDLE & COÛT DE L'INACTION)                       │
│    - WACC TotalEnergies : 4.2% [URD/Consensus] │ Hurdle Rate d'arbitrage : 11.0%       │
│    - TRI / IRR (Base Case sur 5 ans) : 26.4% (marge de sécurité de +15.4 pts vs Hurdle)│
│    - Délai de récupération actualisé (Discounted Payback) : 3.2 ans (Cash positif Y4). │
│    - Coût de l'inaction sur 3 ans : -310 M€ (érosion de la marge de raffinage vs pairs │
│      numérisés, pénalités de déséquilibre réseau et perte d'attractivité des talents). │
│                                                                                        │
│ 6. RISKS REGISTER & KILL CRITERIA AUDITABLES (STOP RULES)                              │
│    Maîtrise des 4 modes d'échec : Talent flight (grille tech), Sabotage managers (WIIFM│
│    & assouplissement cibles), Gouvernance lag (consultation précoce CSE), Impatience.  │
│    Kill Rule M12 : Si adoption active des outils H1 < 45% sur raffineries pilotes à    │
│    M12 -> Gel immédiat de la Tranche 2 (perte strictement bornée à la Tranche 1).      │
│                                                                                        │
│ 7. OPERATING MODEL (HUB & SPOKE PAR HORIZON) & CHANGE MANAGEMENT                       │
│    - Le Hub (Digital Factory Paris + Pangea 5 Pau) détient les "shared rails" & le H3. │
│    - Les Spokes (les 5 branches) déploient le H1 en autonomie guidée.                  │
│    - Forward Deployed Engineers (FDE) projetés sur site pour co-construire le H2.      │
│    - Double binôme hebdo : AI Lead ↔ Métier (terrain) et AI Lead ↔ DF (impact P&L).   │
│    - Formation en 3 Tiers : 95k salariés (Literacy), 3.5k (Praticiens), 250 (Comex).  │
│                                                                                        │
│ 8. THE ASK (RÉSOLUTION OFFICIELLE SOUMISE AU COMEX)                                    │
│    « Approbation de l'enveloppe 3 ans de 195 M€ et libération immédiate de la Tranche 1│
│    de 65 M€ pour les mois 0 à 12. Prochaine revue de passage de jalon en Novembre 2027 │
│    pour autoriser le décaissement de la Tranche 2 (70 M€) sous conditions de KPI. »    │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## PARTIE II : DOSSIER TECHNIQUE, OPÉRATIONNEL & FINANCIER DÉTAILLÉ

### 1. Diagnostic de Maturité & Le Bottleneck Industriel (Session 1)

#### 1.1 Évaluation sur les 5 Piliers de Maturité
* **Business Strategy (Note : 4.0 / 5.0) :** Forte clarté stratégique impulsée par le Comex. TotalEnergies gère une transition complexe : maximiser la rente du pétrole amont à bas coût de production (~5.5 $/b d'OPEX [URD]) tout en investissant 3.5 à 4 Md$/an dans l'Integrated Power [URD] pour atteindre 100 TWh d'électricité nette d'ici 2030 [URD]. L'alignement stratégique de l'IA est évident, mais manque encore de traduction opérationnelle chiffrée par actif.
* **Technology & Data (Note : 2.5 / 5.0) :** Schizophrénie technologique. Le groupe opère l'un des supercalculateurs industriels les plus puissants au monde (**Pangea 5**, contrat de plus de 100 M€ avec Dell & NVIDIA à Pau [URD/Presse 2024]). En revanche, les données industrielles de terrain (OT : systèmes SCADA, automates de raffineries, capteurs de pression de têtes de puits) restent cloisonnées par site dans des formats propriétaires non unifiés.
* **AI Strategy & Experience (Note : 3.0 / 5.0) :** La TotalEnergies Digital Factory (TDF), créée en 2020 au cœur de Paris avec ~300 ingénieurs et data scientists, a démontré la faisabilité de dizaines de PoCs. Toutefois, le groupe peine à industrialiser et répliquer ces solutions au-delà du site pilote initial.
* **Organization & Culture (Note : 2.5 / 5.0) :** Culture d'ingénieurs d'excellence où la culture de sécurité (HSE) prime sur tout. Les directeurs d'usines et chefs de quart en raffinerie ou sur plateforme perçoivent souvent les algorithmes comme des « boîtes noires » risquant de dégrader la sécurité ou de court-circuiter leur autorité opérationnelle.
* **AI Governance (Note : 3.0 / 5.0) :** Robustesse éprouvée en cybersécurité industrielle (sites OIV / directives NIS 2). En revanche, absence d'un inventaire centralisé et auditable des modèles au sens de l'**EU AI Act** (dont l'Annexe III classe explicitement la gestion des réseaux énergétiques et des sites industriels critiques en « haut risque »).

#### 1.2 Positionnement sur les 5 Stades de Readiness
* **Position Actuelle : STADE 3 — IMPLEMENTING (Build & Run)**
  * *Diagnostic :* Le groupe se trouve exactement dans le piège décrit en cours : les coûts de développement et d'infrastructure s'accumulent (infrastructures Pangea, coûts de structure TDF), mais la valeur nette dégagée au P&L consolidé reste diffuse (seules 23% des entreprises à ce stade constatent un impact P&L significatif [Benchmark BCG/McKinsey]).
* **Cible du Plan : STADE 4 — SCALING**
  * Le passage au stade 4 s'opère par la standardisation de la plateforme de données et l'institutionnalisation d'un modèle d'exploitation évitant la réinvention de la roue à chaque actif industriel.

#### 1.3 Le Bottleneck Structurel Identifié
> **LE BOTTLENECK DU GROUPE : La contextualisation et la circulation des données industrielles temps réel (OT/IT) sous contrainte critique de sûreté.**  
> TotalEnergies produit plus de 2.53 Mboe/j de pétrole et gaz et raffine 1.53 Mb/j [URD 2025]. Chaque actif génère des millions de données brutes non standardisées. Sans une couche logicielle unifiée de contextualisation industrielle (Data Fabric temps réel), déployer un algorithme de maintenance sur une 2ème raffinerie coûte aussi cher que sur la 1ère.

---

### 2. Modèle Opérationnel Cible & Gouvernance (Session 2)

#### 2.1 Justification du Modèle selon les 3 Facteurs du Cours
1. **Facteur Taille & Complexité :** ~100 000 salariés dans 120 pays répartis sur 5 branches aux réalités d'affaires diamétralement opposées (pétrole offshore lourd vs trading électrique milliseconde). Le CoE unique centralisé s'effondrerait sous le poids de la coordination.
2. **Facteur Exposition Réglementaire :** Maximale. Risques d'accidents industriels majeurs (sites SEVESO seuil haut), contraintes environnementales strictes, et sanctions de l'EU AI Act (jusqu'à 35 M€ ou 7% du CA mondial). Le modèle fédéré autonome non contrôlé est strictement interdit.
3. **Facteur Empreinte des Talents :** Forte concentration des compétences IA à Paris (TDF) et à Pau (CSTJF), mais rareté absolue de data scientists au sein des raffineries provinciales ou des filiales internationales.

**Recommandation Formelle : Modèle Hub-and-Spoke Hybride Asymétrique articulé par Horizons.**

```
                            ┌───────────────────────────────────────────────┐
                            │               COMEX / SPONSORS                │
                            │   P. Pouyanné, CFO, DG des 5 Branches Métier   │
                            │        Revue mensuelle & seuils de tranche    │
                            └───────────────────────┬───────────────────────┘
                                                    │
                            ┌───────────────────────▼───────────────────────┐
                            │                 LE HUB IA                     │
                            │   Digital Factory (Paris) + CSTJF (Pau/Pangea)│
                            │ • Shared Rails : Core Platform & Data Fabric  │
                            │ • Registre Unique & Audit EU AI Act           │
                            │ • Pôle R&D d'Excellence Rupture (H3)          │
                            └───────────────────────┬───────────────────────┘
                                                    │
                 ┌──────────────────────────────────┼──────────────────────────────────┐
                 │ Shared Rails (API sécurisées)    │ Shared Rails                     │ Shared Rails
                 ▼                                  ▼                                  ▼
    ┌─────────────────────────┐        ┌─────────────────────────┐        ┌─────────────────────────┐
    │       SPOKE E&P         │        │     SPOKE RAFFINAGE     │        │  SPOKE POWER & TRADING  │
    │ Déploiement H1 autonome │        │ Déploiement H1 autonome │        │ Déploiement H1 autonome │
    │ ─── ─── ─── ─── ─── ─── │        │ ─── ─── ─── ─── ─── ─── │        │ ─── ─── ─── ─── ─── ─── │
    │ Squads H2 mixtes avec   │        │ Squads H2 mixtes avec   │        │ Squads H2 mixtes avec   │
    │ FDE (Forward Deployed)  │        │ FDE (Forward Deployed)  │        │ FDE (Forward Deployed)  │
    │ [Binôme Métier ↔ DF]    │        │ [Binôme Métier ↔ DF]    │        │ [Binôme Métier ↔ DF]    │
    └─────────────────────────┘        └─────────────────────────┘        └─────────────────────────┘
```

#### 2.2 Rôles des Forward Deployed Engineers (FDE)
Plutôt que de garder les ingénieurs d'élite à la Tour Coupole ou à la Digital Factory de Paris, TotalEnergies crée un détachement de **Forward Deployed Engineers (FDE)** :
* Des binômes ingénieur IA / data architecte sont projetés sur le terrain (ex : Raffinerie de Normandie à Gonfreville, complexe d'Anvers, trading desk de Genève) pour des immersions de 6 à 9 mois.
* Ils co-développent les solutions H2 directement avec les ingénieurs procédés et chefs de quart, garantissant l'adaptation parfaite aux contraintes de sécurité physique.

#### 2.3 Le Double Binôme Hebdomadaire Obligatoire
Pour éliminer les deux risques mortels identifiés en cours (*Ivory Tower* et *Absence de capture P&L*) :
1. **Binôme Opérationnel : AI Product Owner (Hub) ↔ Business Translator (Métier de branche)**  
   *Cadence :* Revue hebdomadaire de 30 minutes.  
   *Mission :* Ajuster les fonctionnalités aux réalités du terrain et traiter immédiatement les points de friction d'adoption.
2. **Binôme Financier : AI Product Owner ↔ Finance Business Partner (Direction Financière)**  
   *Cadence :* Revue bi-hebdomadaire.  
   *Mission :* **Règle d'or du cours** : toute initiative mise en production doit faire l'objet d'un suivi comptable auditable par la DF. Le contrôleur de gestion trace les économies réelles d'OPEX ou les gains de marge sur les lignes analytiques de l'actif concerné.

---

### 3. Portefeuille Complet : 11 Cas d'Usage par Horizon (Session 2)

Pour refléter la diversité d'un major multi-énergies, le portefeuille est structuré en **3 à 4 cas d'usage par horizon**, couvrant l'ensemble des branches :

```
                        RÉPARTITION DU CAPITAL IA TOTALENERGIES
                       ┌───────────────────────────────────────┐
                       │   H1 : 65%   │   H2 : 25%   │ H3 : 10%│
                       └───────────────────────────────────────┘
```

#### 3.1 HORIZON 1 : Core Optimization (65% de l'enveloppe = 126.75 M€ sur 3 ans)
*Critères d'éligibilité : Processus métier inchangé, client inchangé, technologie éprouvée, rentabilité < 12 mois.*

1. **Cas H1.1 — APM-SEVESO : Maintenance Prédictive & Optimisation Énergétique (Raffinage-Chimie)**
   - *Périmètre :* 1.53 Mb/j de brut raffiné sur 5 plateformes majeures (Normandie, Donges, Feyzin, Anvers, Leuna) [URD].
   - *Technologie & Sourcing :* **Blend** (Plateforme de contextualisation Cognite Data Fusion + modèles séries temporelles internes TDF).
   - *Impact P&L :* Réduction de 1.5% de la facture énergétique des fours (-25 M€/an) [Benchmark McKinsey Energy] et baisse de 15% des arrêts non planifiés de compresseurs critiques (-20 M€/an) [Benchmark Gartner].
   - *Gain annuel attendu à M24 :* **+45 M€/an**.
2. **Cas H1.2 — WellOps AI : Surveillance Préventive des Pompes ESP & Forage Sécurisé (E&P)**
   - *Périmètre :* 2.53 Mboe/j de production amont (actifs offshore profonds Brésil, Angola, Mer du Nord) [URD].
   - *Technologie & Sourcing :* **Blend** (Capteurs IoT haute pression Schlumberger/Baker Hughes + modèles ML de détection d'anomalies).
   - *Impact P&L :* Détection 72h à l'avance du colmatage ou de la surchauffe des pompes de fond, évitant l'arrêt de puits représentant 0.5% de la production journalière.
   - *Gain annuel attendu à M24 :* **+35 M€/an**.
3. **Cas H1.3 — SmartStation & EV-Uptime : Maintenance Prédictive Bornes & Yield Retail (Marketing & Services)**
   - *Périmètre :* Réseau de 15 000 stations-service et 60 000 points de charge électrique déployés en Europe [URD].
   - *Technologie & Sourcing :* **Buy / Adapt** (SaaS de monitoring IoT de bornes EV couplé au CRM client TotalEnergies).
   - *Impact P&L :* Hausse du taux de disponibilité technique des bornes de recharge rapide de 91% à 98.5% (+15 M€ de marge électrique vendue) et optimisation automatisée des réassorts boutique (-8 M€ de BFR).
   - *Gain annuel attendu à M24 :* **+23 M€/an**.
4. **Cas H1.4 — Enterprise Contract & Compliance Copilot (Corporate / Legal / Trading)**
   - *Périmètre :* 100 000 contrats annuels (affrètement maritime GNL, baux miniers, contrats d'achat d'électricité PPA).
   - *Technologie & Sourcing :* **Buy** (Microsoft 365 Copilot & Azure OpenAI sécurisé en tenant souverain dédié).
   - *Impact P&L :* Réduction de 40% du temps de revue des clauses de risque juridique pour 600 juristes et acheteurs, et reporting CSRD automatisé.
   - *Gain annuel attendu à M12 :* **+12 M€/an** (gain de productivité interne valorisé).

#### 3.2 HORIZON 2 : Adjacent Growth & Augmented Decisions (25% de l'enveloppe = 48.75 M€ sur 3 ans)
*Critères d'éligibilité : Nouveaux processus hybrides, décision augmentée, technologie récente, création de valeur en 1 à 3 ans.*

1. **Cas H2.1 — PowerFlow : Dispatching Dynamique & Trading Algorithmique Hybride (Integrated Power & Trading)**
   - *Périmètre :* 34.1 GW de capacité renouvelable brute et 48.1 TWh d'électricité produite [URD 2025].
   - *Technologie & Sourcing :* **Blend** (Modèles météo européens ECMWF + algorithmes d'apprentissage par renforcement propriétaires TotalEnergies Trading).
   - *Impact P&L :* Arbitrage temps réel entre injection directe sur le réseau, stockage en batteries BESS (systèmes Saft) et vente sur EPEX SPOT pour capturer un spread moyen de +2.2 €/MWh et annuler les pénalités de déséquilibre.
   - *Gain annuel attendu à M36 :* **+45 M€/an** [Benchmark Wood Mackenzie Power].
2. **Cas H2.2 — LNG Marine Optimizer : Routage Météo & Arbitrage Spatial Flottant (Trading & Shipping)**
   - *Périmètre :* Flotte de ~40 méthaniers transportant 43.9 Mt de GNL par an [URD 2025].
   - *Technologie & Sourcing :* **Blend** (Données satellites météo marine + jumeau thermodynamique des cuves cryogéniques des navires).
   - *Impact P&L :* Minimisation du gaz évaporé (*boil-off gas*) et réorientation dynamique des cargaisons en mer vers les terminaux offrant le meilleur différentiel de prix Asie vs Europe (JKM vs TTF).
   - *Gain annuel attendu à M36 :* **+25 M€/an**.
3. **Cas H2.3 — AUSEA Automated Vision : Détection & Quantification Autonome du Méthane (HSE & OneTech)**
   - *Périmètre :* Surveillance continue de 100% des sites amont et gaziers mondiaux pour atteindre l'objectif groupe "near-zero methane emissions by 2030" [URD].
   - *Technologie & Sourcing :* **Build / Blend** (Capteurs spectrométriques miniatures AUSEA brevetés par TotalEnergies + analyse d'images par Computer Vision).
   - *Impact P&L :* Réduction immédiate des pertes de gaz commercialisable (+10 M€/an) et évitement des pénalités environnementales carbone UE/US (+8 M€/an).
   - *Gain annuel attendu à M24 :* **+18 M€/an**.
4. **Cas H2.4 — Circular Chemistry Yield (Raffinage & Pétrochimie)**
   - *Périmètre :* Vapocraqueurs et usines de polymères (sites de Normandie, Carling, Feluy).
   - *Technologie & Sourcing :* **Blend** (FDE projetés en usine chimique + modèles prédictifs de cinétique chimique).
   - *Impact P&L :* Optimisation en temps réel de la marche des fours de vapocraquage en fonction de la composition variable des charges d'huiles de pyrolyse issues de déchets plastiques recyclés.
   - *Gain annuel attendu à M36 :* **+20 M€/an**.

#### 3.3 HORIZON 3 : Transformational & Moonshots (10% de l'enveloppe = 19.5 M€ sur 3 ans)
*Critères d'éligibilité : Nouveaux modèles d'affaires, rupture scientifique fondamentale, valeur optionnelle à 3-5 ans, KPIs non financiers (brevets, précision, vitesse de découverte).*

1. **Cas H3.1 — GeoMol SAF : Découverte Accélérée de Catalyseurs pour Carburants Aériens Durables (R&D / Pangea 5)**
   - *Périmètre :* Conception assistée par IA de catalyseurs pour transformer le CO2 et l'hydrogène vert en e-kérosène (mandat ReFuelEU Aviation).
   - *Technologie & Sourcing :* **Build** (Simulation quantique et Physics-Informed Neural Networks - PINNs développés sur les nœuds GPU de Pangea 5 avec NVIDIA).
   - *KPIs H3 :* Facteur 10x sur la vitesse de criblage virtuel des molécules ; 2 brevets internationaux déposés avant M24. Option stratégique majeure sur le marché des SAF à l'horizon 2030.
2. **Cas H3.2 — Subsurface PINNs : Modélisation Autonome des Réservoirs de Séquestration Carbone (CCS)**
   - *Périmètre :* Projets géants de stockage de CO2 (Northern Lights en Norvège, Aramis aux Pays-Bas) [URD].
   - *Technologie & Sourcing :* **Build** (Modélisation de la dynamique des fluides souterrains par IA générative géophysique au CSTJF Pau).
   - *KPIs H3 :* Réduction de 70% du temps d'inversion sismique 4D pour garantir l'intégrité du confinement du CO2 face aux autorités environnementales européennes.
3. **Cas H3.3 — Autonomous Virtual Power Plant (VPP) & V2G Décentralisé (Integrated Power / M&S)**
   - *Périmètre :* Agrégation dynamique de 500 000 actifs distribués (batteries domestiques, véhicules électriques en charge bidirectionnelle V2G, toitures solaires B2B).
   - *Technologie & Sourcing :* **Partner / Blend** (Architecture agentique autonome négociant de micro-services réseau avec les gestionnaires de réseau RTE et TenneT).
   - *KPIs H3 :* Preuve de concept validée sur 10 000 véhicules avant M24 ; business model novateur d'Energy-as-a-Service générant des revenus récurrents de capacité.

---

#### 3.4 The Sequencing Canvas (Tableau de Séquençage du Portefeuille)

| # | Code | Initiative | Horizon | Part Budget | Dépendance ("Thin Slice") | Sourcing | Premier Jalon Clé | Propriétaire & Échéance |
| :---: | :--- | :--- | :---: | :---: | :--- | :---: | :--- | :--- |
| **0** | **PLAT** | **Plateforme Industrielle Data & MLOps** | Socle | 20.0% | Slice OT sur 2 raffineries & 10 parcs solaires | Blend | Connecteurs SCADA opérationnels | CTO Hub — M6 |
| **1** | H1.1 | **APM-SEVESO Raffinage** | H1 | 18.0% | Dépendance PLAT (Slice Raffinerie) | Blend | Pilote en ligne à Normandie | EVP Raffinage — M9 |
| **2** | H1.2 | **WellOps Amont Pétrolier** | H1 | 15.0% | Dépendance PLAT (Slice Offshore) | Blend | Algorithme déployé sur 20 puits | EVP E&P — M9 |
| **3** | H1.3 | **SmartStation & Bornes EV** | H1 | 8.0% | Slice API Réseau Bornes M&S | Buy/Adapt | Taux d'uptime à 98% sur 2 000 bornes | EVP M&S — M8 |
| **4** | H1.4 | **Enterprise Copilot & Legal** | H1 | 4.0% | Slice Documents Juridiques | Buy | Déploiement sécurisé 600 juristes | Directeur Juridique — M4 |
| **5** | H2.1 | **PowerFlow Dispatching & Trading** | H2 | 12.0% | Dépendance PLAT (Slice Marché EPEX) | Blend | Algo en production trading desk Paris | EVP Power — M15 |
| **6** | H2.2 | **LNG Marine Optimizer** | H2 | 6.0% | Slice Données Météo & AIS Navires | Blend | Test sur 5 méthaniers transatlantiques | VP Shipping — M14 |
| **7** | H2.3 | **AUSEA Vision Méthane** | H2 | 4.0% | Capteurs spectrométriques AUSEA | Build/Blend | Détection autonome sur 10 sites gaziers | VP HSE — M10 |
| **8** | H2.4 | **Circular Chemistry Yield** | H2 | 3.0% | Dépendance PLAT (Slice Vapocraqueur) | Blend | Gain de rendement validé à Carling | VP Chimie — M16 |
| **9** | H3.1 | **GeoMol SAF Pangea 5** | H3 | 4.0% | Slice HPC GPU Pangea 5 Pau | Build | 1ère molécule virtuelle criblée | VP R&D OneTech — M18 |
| **10**| H3.2 | **Subsurface PINNs CO2** | H3 | 3.5% | Slice Données Sismiques Northern Lights | Build | Modèle géophysique 4D calibré | Dir. Climat & CCS — M18 |
| **11**| H3.3 | **Autonomous VPP & V2G** | H3 | 2.5% | Slice Données Réseau Borne EV | Partner | Pilote 1 000 véhicules connectés | VP New Ventures — M20 |
| — | **ENAB** | **AI Academy & Change Management** | Enabler| 5.0% | Aucune (Lancement immédiat dès M1) | Build | 100% Comex formé, 1 500 certifiés T2 | CHRO — M6 |
| **TOT**| — | **Total Portefeuille 3 Ans** | **100%** | **195 M€** | *Financement strict des fondations par cas* | — | *Libération Tranche 1 ferme (65 M€)* | **Comex Sponsor** |

---

### 4. Ingénierie Financière : Balance CAPEX / OPEX, DCF & Scénarios (Session 3)

#### 4.1 Répartition Détaillée de l'Enveloppe : La Balance CAPEX / OPEX
La distinction entre CAPEX et OPEX est l'exigence numéro 1 posée par le Comex. Conformément aux normes IFRS (notamment IAS 38 pour l'immatériel) :
* **Sont comptabilisés en CAPEX :** Les acquisitions d'actifs physiques durables (serveurs, accélérateurs GPU Pangea 5, capteurs AUSEA) ainsi que les coûts de développement interne directement attribuables à la conception de la plateforme logicielle propriétaire industrielle.
* **Sont comptabilisés en OPEX :** Les consommations de calcul Cloud as-a-Service (Azure/AWS), les coûts récurrents d'inférence des modèles (tokens LLM), les abonnements aux licences SaaS, les salaires récurrents des équipes et FDE, la maintenance MLOps, les programmes de formation (AI Academy) et les frais de conseil en conduite du changement.

##### Tableau de Ventilation CAPEX / OPEX sur 3 Ans et 5 Ans (en M€)

| Catégorie Budgétaire | Description Technique & Fonctionnelle | Traitement Comptable | An 1 (M€) | An 2 (M€) | An 3 (M€) | **Total 3 Ans** | An 4 (M€) | An 5 (M€) | **Total 5 Ans** |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1. Hardware & Infrastructure HPC** | Extension GPU/NVMe Pangea 5 à Pau [URD] & serveurs edge sécurisés sur site | **CAPEX** (Corporel) | 18.0 | 8.0 | 4.0 | **30.0** | 3.0 | 2.0 | **35.0** |
| **2. Core Data Platform & Connecteurs OT** | Architecture Data Fabric temps réel & intégration SCADA (IAS 38) | **CAPEX** (Immatériel) | 16.0 | 14.0 | 10.0 | **40.0** | 2.0 | 1.0 | **43.0** |
| **3. Capteurs & Matériel IoT AUSEA** | Drones et instrumentation optique pour détection méthane | **CAPEX** (Corporel) | 8.0 | 4.0 | 3.0 | **15.0** | 1.0 | 1.0 | **17.0** |
| **SOUS-TOTAL CAPEX** | *Investissements capitalisables* | **CAPEX** | **42.0** | **26.0** | **17.0** | **85.0 (43.6%)**| **6.0** | **4.0** | **95.0 (33.0%)**|
| **4. Cloud Compute & Inférence LLM** | Burst Cloud Azure/AWS, consommation API modèles fondation Mistral/OpenAI | **OPEX** | 5.0 | 9.0 | 11.0 | **25.0** | 12.0 | 13.0 | **50.0** |
| **5. Licences Logicielles SaaS & MLOps** | Cognite Data Fusion, monitoring de dérive, catalogues de métadonnées | **OPEX** | 6.0 | 9.0 | 10.0 | **25.0** | 10.0 | 10.0 | **45.0** |
| **6. Talents & FDE (Masse Salariale)** | 60 experts IA/data et ingénieurs FDE projetés sur site | **OPEX** | 9.0 | 12.0 | 14.0 | **35.0** | 15.0 | 15.0 | **65.0** |
| **7. Change Management & Gouvernance** | AI Academy (3 tiers), coaching, comitologie, audits conformité EU AI Act | **OPEX** | 3.0 | 14.0 | 8.0 | **25.0** | 4.0 | 4.0 | **33.0** |
| **SOUS-TOTAL OPEX** | *Charges d'exploitation récurrentes* | **OPEX** | **23.0** | **44.0** | **43.0** | **110.0 (56.4%)**| **41.0**| **42.0**| **193.0 (67.0%)**|
| **TOTAL GÉNÉRAL DÉCAISSEMENTS** | **Enveloppe globale par an** | **TOTAL** | **65.0** | **70.0** | **60.0** | **195.0 M€** | **47.0**| **46.0**| **288.0 M€** |

*Structure de décaissement par tranche :*
* **Tranche 1 (Mois 0 à 12) : 65.0 M€** (42 M€ CAPEX + 23 M€ OPEX) — Déblocage immédiat.
* **Tranche 2 (Mois 12 à 24) : 70.0 M€** (26 M€ CAPEX + 44 M€ OPEX) — Conditionnée au Kill Criterion M12.
* **Tranche 3 (Mois 24 à 36) : 60.0 M€** (17 M€ CAPEX + 43 M€ OPEX) — Conditionnée aux métriques d'EBIT M24.

---

#### 4.2 Tableau des Flux de Trésorerie Actualisés (DCF) sur 5 Ans (Base Case)
*Hypothèses financières retenues :*
* **WACC Corporate TotalEnergies :** **4.2%** [URD 2024 / Modèles d'analystes consensus].
* **Prime de risque technologique & d'exécution :** **+6.8%** [Benchmark cours Module 3 pour les programmes IA industriels].
* **Hurdle Rate (Taux d'actualisation r) :** **11.0%** (Arrondi conservateur de 4.2% + 6.8%).
* *Facteur d'actualisation :* $DF_t = \frac{1}{(1 + 0.11)^t}$.

| Année (t) | CAPEX (M€) | OPEX (M€) | Décaissement Total (M€) | Gains Bruts P&L (M€) | Cash Flow Net (M€) | DF @ 11.0% | Cash Flow Actualisé (PV) | Cumul Cash Net (M€) | Cumul PV (M€) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **0 (M0-M1)** | −42.0 | −23.0 | **−65.0** | 0.0 | **−65.0** | 1.000 | **−65.0** | −65.0 | **−65.0** |
| **1 (M12)** | −26.0 | −44.0 | **−70.0** | +25.0 | **−45.0** | 0.901 | **−40.5** | −110.0 | **−105.5** |
| **2 (M24)** | −17.0 | −43.0 | **−60.0** | +85.0 | **+25.0** | 0.812 | **+20.3** | −85.0 | **−85.2** |
| **3 (M36)** | −6.0 | −41.0 | **−47.0** | +142.0 | **+95.0** | 0.731 | **+69.4** | +10.0 | **−15.8** |
| **4 (M48)** | −4.0 | −42.0 | **−46.0** | +185.0 | **+139.0** | 0.659 | **+91.6** | +149.0 | **+75.8** |
| **5 (M60)** | −3.0 | −43.0 | **−46.0** | +210.0 | **+164.0** | 0.593 | **+97.3** | +313.0 | **+173.1** |

---

#### 4.3 Métriques Financières Clés & Justification des Formules
1. **Net Present Value (NPV / VAN) à 5 ans :**
   $$NPV = \sum_{t=1}^{5} \frac{CF_t}{(1 + 0.11)^t} - I_0 = 238.1 - 65.0 = \mathbf{+173.1\ M€}$$
   *(À l'horizon strict de 3 ans du memo Comex, la NPV s'élève à **+68.2 M€** en intégrant la valeur terminale normalisée des gains récurrents).*
2. **Internal Rate of Return (IRR / TRI) :** **26.4%**.
   *Interprétation :* Le taux de rentabilité interne dépasse largement le Hurdle rate de 11.0% et le WACC de 4.2%. Le projet reste créateur de valeur tant que le coût du capital ne dépasse pas 26.4%.
3. **Payback Simple :** **2.9 ans** (le cumul brut de trésorerie redevient positif au cours de la 3ème année : $2 + \frac{85}{95}$).
4. **Discounted Payback (Délai de récupération actualisé) :** **3.2 ans** (la valeur actualisée cumulée bascule en territoire positif au début de l'année 4 : $3 + \frac{15.8}{91.6}$).
5. **Return on Investment (ROI nominal sur 5 ans) :**
   $$ROI = \frac{\text{Gains Cumulés} - \text{Coûts Cumulés}}{\text{Coûts Cumulés}} = \frac{647.0 - 334.0}{334.0} = \mathbf{93.7\%}$$

---

#### 4.4 Analyse des 3 Scénarios & Calcul de l'Espérance de Valeur (EV)
Le cours interdit la fausse précision d'un scénario unique. Nous modélisons trois trajectoires avec probabilités explicites :

| Scénario | Proba | Hypothèses Sous-Jacentes (Gains & Coûts) | NPV @ 11% (3 ans) | NPV @ 11% (5 ans) | Réponse Décisionnelle du Comex |
| :--- | :---: | :--- | :---: | :---: | :--- |
| **Downside (Pessimiste)**| **20%** | Forte résistance en raffinerie, intégration OT retardée de 12 mois, adoption à 35%. Gains limités à 40% du nominal. Dérive des coûts Cloud (+20%). | **−18.2 M€** | **−5.4 M€** | **Loss Cap activé :** Arrêt immédiat des cas non rentables à M12 via les Kill Criteria. La perte maximale nette reste bornée à la Tranche 1. |
| **Base Case (Nominal)**| **60%** | Déploiement nominal des 11 cas d'usage, adoption conforme aux jalons (60% des cibles formées à M18), gains opérationnels nominaux. | **+68.2 M€** | **+173.1 M€** | **Exécution nominale :** Déblocage des Tranches 2 et 3 selon le calendrier contractuel. |
| **Upside (Optimiste)**| **20%** | Succès rapide de PowerFlow (spread capté à +3.5 €/MWh), accélération de la réplication internationale et démarrage précoce des SAF GeoMol. | **+135.4 M€** | **+295.0 M€** | **Option de réinvestissement :** Réallocation d'une fraction des gains H1 vers l'accélération des projets H3. |
| **VALEUR ESPÉRÉE (EV)**| **100%**| $\sum (\text{Proba} \times \text{NPV})$ | **+64.4 M€** | **+161.8 M€** | **Dossier hautement rentable et résilient au risque d'exécution.** |

---

#### 4.5 Le Coût Chiffré de l'Inaction (Cost of Doing Nothing)
Refuser d'investir ne maintient pas le statu quo : c'est accepter une détérioration continue de la position concurrentielle de TotalEnergies face aux autres "Supermajors" (Shell, BP, ExxonMobil) et aux utilities intégrées (Engie, Iberdrola, Enel) :

1. **Érosion de la Marge de Raffinage Européenne vs Pairs Numérisés :**
   * *Méthode :* TotalEnergies raffine ~1.53 Mb/j [URD]. L'écart de coût énergétique et d'arrêts non planifiés avec une raffinerie optimisée par IA (ex : Shell Pernis ou BP Rotterdam) est évalué à **0.25 $/baril** [Benchmark Wood Mackenzie / McKinsey Energy].
   * *Calcul :* $1\,530\,000\ \text{barils/j} \times 365\ \text{j} \times 0.25\ \$/\text{b} = 139.6\ \text{M}\$/\text{an} \approx 130\ \text{M€/an}$.
   * *Impact sur 3 ans :* **−150 M€** (en tenant compte d'un décrochage progressif sur le parc européen).
2. **Pénalités de Déséquilibre & Sous-Optimisation du Trading Renouvelable :**
   * *Méthode :* Production électrique de 48.1 TWh/an, dont ~31 TWh renouvelables intermittents [URD 2025]. Sans trading algorithmique en temps réel, les pénalités de déséquilibre payées aux gestionnaires de réseau (RTE en France, TenneT en Allemagne) s'élèvent en moyenne à **1.5 €/MWh** [Benchmark CRE / EPEX].
   * *Calcul :* $31\ \text{TWh} \times 1.5\ \text{€/MWh} \approx 46.5\ \text{M€/an}$.
   * *Impact sur 3 ans :* **−90 M€**.
3. **Coût de Turnover & Fuite des Talents Techniques Clés :**
   * *Méthode :* Les ingénieurs réservoir, géophysiciens et data scientists quittent l'entreprise face à des outils obsolètes. Remplacer 150 profils rares coûte environ 1.5x le salaire annuel chargé + perte de vélocité des projets R&D [Benchmark BCG Tech Talent 2026].
   * *Impact sur 3 ans :* **−70 M€**.
* **COÛT TOTAL CONSOLIDÉ DE L'INACTION SUR 3 ANS : −310 M€.**

---

### 5. Plan de Conduite du Changement & Risques en 3 Volets (Module 5 / Slides 166-202)

#### 5.1 Volet 1 : Registre des Risques sur les 4 Modes d'Échec du Cours

| Mode d'Échec (Slide 166-170) | Signal d'Alerte Précoce | Stratégie d'Atténuation (Mitigation) | Responsable (Owner) |
| :--- | :--- | :--- | :--- |
| **1. Talent Flight (Fuite des talents)** | Taux d'attrition > 10% ou offres d'embauche refusées sur les postes IA à la Digital Factory et à Pau. | Création d'une grille de rémunération tech hors-statut pétrolier ; sanctuarisation de 20% du temps des experts sur des projets de rupture H2/H3 stimulants. | **CHRO + Chief AI Officer** |
| **2. Middle-Management Sabotage (Sabotage des managers)** | Taux d'utilisation stagnant sur un site ; maintien des doubles vérifications manuelles ; contournement de l'outil. | Co-conception des interfaces avec les chefs de quart ; assouplissement temporaire des KPIs de production pendant le « learning dip » ; script WIIFM clair. | **Directeurs des Branches Métier (EVP)** |
| **3. Governance Lag & Risque CSE (Blocage juridique)** | Refus d'avis du CSE ; demandes d'expertises judiciaires ; développement de Shadow AI non tracé. | Consultation formelle anticipée du CSE (application stricte de la jurisprudence Nanterre 2025) ; registre central EU AI Act ; formation obligatoire Art. 4. | **Secrétaire Général + Directeur Juridique** |
| **4. Comex Impatience (Impatience de la direction)** | Remise en cause du budget au mois 8 face au creux de cash flow de la courbe en J. | Contrat d'objectifs pré-validé à 12/24/36 mois ; livraison obligatoire d'un quick win visible avant M6 (Copilot Contrats) ; dashboard mensuel axé sur l'usage. | **CFO + Lead Transformation IA** |

---

#### 5.2 Volet 2 : Cartographie des Acteurs & Inversion de la Cadence de Communication

```
                   POUVOIR SUR L'ADOPTION
                              ▲
                              │
               [GARDIENS]     │     [SPONSORS]
               CSE, HSE, DPO, │     Patrick Pouyanné,
               Affaires Réglem.│     Comex, DG de Branches
             ─────────────────┼────────────────────────►
               [ADOPTEURS]    │     [TRANSLATORS]        INTÉRÊT DANS
               Opérateurs,    │     Directeurs de sites, LE PROGRAMME
               Chefs de quart,│     Chefs d'installations,
               Traders terrain│     Responsables maintenance
                              │
```

##### Inversion Rigoureuse de la Pyramide de Communication (Slide 176)
Le cours prouve que la cadence traditionnelle est inversée (un deck de 40 pages envoyé au Comex, et un simple email laconique envoyé au terrain). Nous appliquons la méthode vertueuse :

| Classe d'Acteurs | Cadence & Format Retenus | Émetteur Privilégié (The Messenger) | Contenu & Objectif Clé |
| :--- | :--- | :--- | :--- |
| **Sponsors (Comex)** | **Mensuel** — Dashboard synthétique d'**1 page** (usage, cash capté, incidents). | Chief AI Officer & CFO | Valider la trajectoire financière, lever les blocages inter-branches et arbitrer les tranches. |
| **Translators (Management intermédiaire)** | **Hebdomadaire** — Huddle opérationnel de 30 min + boîte à outils (toolkit). | Directeurs de sites industriels | Donner du sens opérationnel, analyser les frictions et rassurer sur les objectifs du trimestre. |
| **Adopters (Le terrain / Usines)** | **Quotidien / Par shift** — Échanges de 15 min au poste + canal Teams direct. | Champions locaux issus du terrain | Entraînement pratique, démonstrations concrètes par les pairs et recueil direct des irritants. |
| **Guardians (CSE, HSE, DPO)** | **Mensuel** — Commission de suivi de transition numérique & sécurité. | Secrétaire Général & DRH | Présenter l'avancement technique, vérifier l'absence d'impact négatif sur la charge de travail et la sûreté. |

---

#### 5.3 Volet 3 : Plan de Compétences 3 Tiers & Kill Criteria Implacables

##### L'AI Academy en 3 Niveaux (Slide 180)
1. **Tier 1 — All-Employee Literacy (95 000 collaborateurs) :**  
   *Contenu :* Module interactif de 3 heures sur l'utilisation sécurisée de l'IA, la protection des données sensibles TotalEnergies, les limites des LLM et la conformité à l'Article 4 de l'EU AI Act.
2. **Tier 2 — Practitioner Deep-Dive (3 500 ingénieurs, techniciens & champions) :**  
   *Contenu :* Parcours certifiant de 40 heures sur la reconception des flux de travail industriels, la supervision des modèles prédictifs et l'interaction avec les agents autonomes.
3. **Tier 3 — Executive Coaching (Top 250 Dirigeants & Membres du Comex) :**  
   *Contenu :* Sessions individuelles et en comité restreint pour apprendre à auditer un business case IA, piloter le risque de modèle et incarner l'adoption au sommet de l'entreprise.

##### Les Kill Criteria Pré-Négociés (Règles d'Arrêt Fermes - Slide 182)
Conformément aux règles du cours (*« Décider avant de lancer ce qui nous fera arrêter »*), voici les seuils d'arrêt contractuels :

| Échéance | Périmètre Évalué | Métrique & Seuil Critique d'Arrêt | Décideur Habilité | Action Immédiate en Cas de Non-Respect |
| :---: | :--- | :--- | :---: | :--- |
| **Mois 12** | **Cas H1.1 (APM-SEVESO)** | Si l'adoption active hebdomadaire des opérateurs en salle de contrôle est **< 45%** sur les sites pilotes. | **CFO & EVP Raffinage** | **Arrêt immédiat de la réplication** ; gel de la Tranche 2 ; réaffectation des capitaux vers l'amont pétrolier. |
| **Mois 18** | **Cas H2.1 (PowerFlow)** | Si le gain net incrémental de trading mesuré par la DF est **< 10 M€** par rapport à la baseline conventionnelle. | **Directeur Trading & CFO** | **Démantèlement de l'algorithme** ; transfert des FDE vers l'optimisation maritime GNL. |
| **Mois 24** | **Ensemble du Portefeuille** | Si le coût d'inférence et d'hébergement unitaire (Run/Inférence) dépasse **70% de la valeur P&L brute** générée par le cas d'usage. | **Steering Committee IA** | **Décommissionnement sans condition** du cas d'usage pour éviter la dérive des coûts Cloud récurrents. |

---

### 6. Guide de Soutenance Orale (Face au CEO Patrick Pouyanné)

#### 6.1 Conducteur du Pitch de 15 Minutes
* **00:00 – 02:30 | L'Arbitrage Stratégique (Thesis) :** Poser la demande ferme d'approbation (195 M€, Tranche 1 de 65 M€), le positionnement multi-énergies et l'urgence de franchir le bottleneck des données OT.
* **02:30 – 05:30 | Le Modèle Opérationnel & La Balance CAPEX/OPEX :** Justifier le modèle Hub & Spoke par horizon, le rôle des FDE projetés, et expliciter la balance financière saine (44% CAPEX / 56% OPEX sur 3 ans).
* **05:30 – 09:30 | Le Portefeuille des 11 Cas d'Usage :** Présenter l'équilibre 65-25-10, détailler les cas phares (Raffinage H1, PowerFlow H2, GeoMol Pangea H3) et démontrer la rigueur du Sequencing Canvas ("thin-slicing").
* **09:30 – 12:30 | L'Analyse Financière & Le Coût de l'Inaction :** Démontrer la clearance du Hurdle (TRI 26.4% vs 11%), le Discounted Payback (3.2 ans) et marteler le coût de l'inaction (−310 M€).
* **12:30 – 14:30 | La Maîtrise des Risques & Les Kill Criteria :** Prouver que 70% de la valeur réside dans les hommes. Présenter la gestion des 4 modes d'échec et la règle d'arrêt formelle à M12.
* **14:30 – 15:00 | The Ask :** Réitérer la résolution soumise au vote du Comex.

#### 6.2 Réponses Blindées aux Questions Sceptiques du Board (Slide 204)
1. **« Quel est le pire des scénarios et combien je perds si votre projet déraille ? »**
   * *Réponse :* « Monsieur le Président, dans notre scénario Downside (retard OT et adoption faible), la perte maximale nette est strictement bornée à **65 M€ (la Tranche 1)** grâce à notre Kill Criterion auditable du 12ème mois. Si l'adoption en raffinerie est inférieure à 45%, la Tranche 2 n'est pas débloquée et le programme est suspendu. »
2. **« Pourquoi me demander 195 M€ alors que Shell et BP achètent des solutions toutes faites auprès de Microsoft et Palantir ? »**
   * *Réponse :* « Parce que nous appliquons la règle d'approvisionnement stricte du cours : nous achetons sur étagère ce qui est banalisé (notre Copilot H1 pour 4% du budget), mais nous construisons en interne notre avantage compétitif (notre algorithme PowerFlow et la simulation Pangea 5). Acheter du standard sur notre cœur de métier reviendrait à payer une rente perpétuelle à un éditeur tout en annulant toute différenciation sur nos marges de trading et de raffinage. »
3. **« Quel est le risque avec les syndicats et le CSE sur des sites SEVESO sensibles ? »**
   * *Réponse :* « Nous avons intégré les enseignements de la jurisprudence Nanterre 2025 : le CSE est formellement consulté dès le mois 1, bien avant les pilotes opérationnels. Par ailleurs, 25 M€ de notre enveloppe sont alloués à la formation et à l'accompagnement des opérateurs, transformant l'IA en un outil de confort et de sécurité physique, et non de réduction d'effectifs. »
