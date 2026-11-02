# Roadmap Projet — Transformation IA TotalEnergies SE

> **Membres de l'équipe :** Alexandre Waerniers, Vincent Lamy, Yoni Mahieddine, Nahel Bachriri  
> **Entreprise :** TotalEnergies SE  
> **Échéance :** Soutenance orale le 16 Novembre 2026 (15 min pitch + 5 min Q&A face au prof incarnant Patrick Pouyanné)  
> **Livrables finaux :** Le Comex Memo (2 pages) + Le Support de Présentation (Slides) + Le Rapport de Fond de Référence

---

## 1. Vision et Méthode de Travail

Pour réussir l'épreuve sans se perdre dans la complexité d'un groupe mondial de 100 000 salariés :

1. **Construire d'abord le Rapport de Fond Complet ("Conditions réelles") :**  
   C'est notre socle de vérité. On y pose méthodiquement tous les diagnostics, les benchmarks concurrentiels, l'architecture des branches, les calculs financiers (CAPEX/OPEX, DCF) et la conduite du changement. Avoir ce document solide garantit que chaque affirmation orale aura une assise inattaquable.
2. **Extraire ensuite le Comex Memo de 2 pages :**  
   Une fois le fond maîtrisé, condenser en 2 pages exécutives (les 7/8 blocs officiels) devient un exercice direct de synthèse, sans jargon ni surcharge de chiffres, centré sur la décision d'investissement.
3. **Concevoir enfin les Slides de Soutenance (15-20 min) :**  
   Impossible de tout projeter : les slides mettront en scène l'arbitrage stratégique macro, le comparatif avec Shell/BP, et un focus narratif fort sur **3 à 4 cas emblématiques**, tout en étant armés pour répondre à n'importe quelle question pointue en Q&A grâce au rapport de fond.

---

## 2. Les 8 Étapes de la Roadmap

```
  Phase 1 : Cadrage & Concurrence ──► Phase 2 : Diagnostic & Bottleneck
                 │                                      │
  Phase 4 : Portefeuille & Séquençage ◄── Phase 3 : Operating Model Cible
                 │
  Phase 5 : Modélisation Financière ──► Phase 6 : Change & Kill Criteria
                                                        │
  Phase 8 : Slides & Soutenance Oral ◄── Phase 7 : Memo Comex (2 pages)
```

---

### ÉTAPE 1 : Cadrage du Groupe & Benchmark Concurrentiel
* **Objectif :** Poser le contexte réel et la pression concurrentielle.
* **Actions :**
  * Cartographier les 5 branches de TotalEnergies (E&P, Integrated Power, Raffinage-Chimie, M&S, Trading) et leurs disparités géographiques et culturelles.
  * Analyser le retard relatif de TotalEnergies face aux déploiements mondiaux de **Shell (partenariat C3 AI)** et de **BP (partenariat Palantir)**.
  * Formaliser l'argument clé pour le Comex : pourquoi Total doit passer d'une logique de PoCs isolés (TDF/Pangea) à une standardisation industrielle.

---

### ÉTAPE 2 : Diagnostic de Maturité & Identification du Bottleneck
* **Objectif :** Diagnostiquer l'état actuel selon les frameworks du cours (Session 1).
* **Actions :**
  * Évaluer TotalEnergies sur les 5 Piliers de Maturité (Stratégie, Data/Tech, Expérience IA, Culture/Orga, Gouvernance).
  * Positionner le groupe sur les 5 Stades (Constat : bloqué au stade 3 *Implementing*, ambition de basculer au stade 4 *Scaling*).
  * Formuler le **Bottleneck structurel unique** : le cloisonnement des données industrielles temps réel (OT/IT) et les contraintes de sûreté critique (SEVESO / EU AI Act Annexe III).

---

### ÉTAPE 3 : Définition de l'Operating Model Cible
* **Objectif :** Structurer l'organisation humaine et technique selon les frameworks du cours (Session 2).
* **Actions :**
  * Justifier le modèle **Hub-and-Spoke par Horizons sur Shared Rails** (via l'arbre de décision : réglementation, dispersion des marchés, maturité).
  * Définir le rôle du Hub (TDF Paris + CSTJF Pau / Pangea 5) vs les Spokes (les 5 branches).
  * Cadrer le dispositif des **Forward Deployed Engineers (FDE)** projetés sur site.
  * Instituer les doubles binômes hebdomadaires obligatoires :
    * Binôme Opérationnel : AI Product Owner ↔ Lead Métier de branche (adoption).
    * Binôme Financier : AI Product Owner ↔ Contrôleur de Gestion / Direction Financière (audit du P&L).

---

### ÉTAPE 4 : Architecture du Portefeuille & Séquençage
* **Objectif :** Répartir les investissements selon les Three Horizons et établir le Sequencing Canvas (Session 2).
* **Actions :**
  * Justifier l'arbitrage macro **65% H1 / 25% H2 / 10% H3** (déviation raisonnée pour accélérer sur l'électricité intégrée).
  * Sélectionner et caractériser les cas d'usage représentatifs par horizon (dont 3 ou 4 cas majeurs qui seront les stars de la présentation orale).
  * Établir le **Sequencing Canvas** : rattachement des fondations par cas d'usage ("thin-slicing", *"a slice, not a lake"*), Build/Buy/Blend, jalons et owners Comex.

---

### ÉTAPE 5 : Modélisation Financière Macro & Analyse du Risque
* **Objectif :** Fournir les chiffres clés attendus par les C-levels (Session 3).
* **Actions :**
  * Définir l'enveloppe d'investissement 3 ans et la trajectoire 5 ans.
  * **Isoler clairement la balance CAPEX vs OPEX** (règles comptables IFRS / IAS 38).
  * Calibrer le **Hurdle Rate** (WACC TotalEnergies ~4.2% + prime de risque tech IA ~6.8% = 11.0%).
  * Modéliser le tableau des flux de trésorerie (DCF) et calculer : NPV, TRI, Payback simple, Discounted Payback.
  * Établir les 3 scénarios (Downside 20%, Base 60%, Upside 20%) avec l'Espérance de Valeur (EV).
  * Chiffrer de manière robuste et défendable le **Coût de l'Inaction (Cost of Doing Nothing)** sur 3 ans.

---

### ÉTAPE 6 : Conduite du Changement & Kill Criteria
* **Objectif :** Démontrer que 70% de la valeur dépend des hommes et des règles de contrôle (Session 4 & Module 5).
* **Actions :**
  * Rédiger le Registre des Risques sur les **4 modes d'échec** (Talent flight, Sabotage middle-management, Retard gouvernance/CSE, Impatience Comex).
  * Inverser la pyramide de communication (dashboard 1 page pour le Comex, huddles ultra-locaux et fréquents pour le terrain).
  * Définir le plan de compétences en **3 Tiers** (All-employee literacy, Practitioners, Executive coaching).
  * Formuler les **Kill Criteria contractuels** à M12, M18 et M24 (Métrique + Seuil + Date + Décideur + Action d'arrêt ferme).

---

### ÉTAPE 7 : Rédaction du Comex Memo Exécutif (2 Pages)
* **Objectif :** Produire le livrable écrit de synthèse décisionnelle (Slide 190).
* **Actions :**
  * Page 1 : Blocs 1 à 4 (Thesis, Portfolio, Envelope & CAPEX/OPEX, Scenarios).
  * Page 2 : Blocs 5 à 8 (Financial clearance, Risks & Kill criteria, Operating Model & Change, The Ask).
  * Respect strict des principes de rédaction : décision dès la première ligne, un chiffre par affirmation, zéro verbiage, aucun schéma d'architecture.

---

### ÉTAPE 8 : Conception du Support de Pitch (15 min) & Préparation Board Q&A
* **Objectif :** Préparer la prestation orale de 15 min + 5 min face à Patrick Pouyanné (Slide 203-206).
* **Actions :**
  * Scénariser les slides avec des titres d'assertion forts (*"Assertion headlines"*).
  * Mettre en valeur le comparatif concurrentiel (Shell / BP) et les 3-4 cas d'usage phares.
  * Répartir le temps de parole entre les membres de l'équipe (Alexandre, Vincent, Yoni, Nahel).
  * Répéter et blinder les réponses aux 3 questions pièges du board (*"Quel est le pire des scénarios ?", "Qu'est-ce qui vous fait arrêter et quand ?", "Pourquoi ne pas attendre ?"*).

---

## 3. État d'Avancement & Prochaine Étape Immédiate

* [x] **Étape 0 :** Cadrage méthodologique et validation de la démarche globale.
* [ ] **Étape 1 (En cours) :** Cadrage approfondi de l'organisation de TotalEnergies & Benchmark concurrentiel (Shell / BP / Equinor).
* [ ] **Étape 2 :** Diagnostic de Maturité & Le Bottleneck.
* [ ] **Étape 3 :** Operating Model Cible & Gouvernance.
* [ ] **Étape 4 :** Portefeuille (Three Horizons) & Sequencing Canvas.
* [ ] **Étape 5 :** Ingénierie Financière (CAPEX/OPEX, DCF, Scénarios, Coût d'inaction).
* [ ] **Étape 6 :** Conduite du Changement & Kill Criteria.
* [ ] **Étape 7 :** Rédaction du Comex Memo (2 pages).
* [ ] **Étape 8 :** Support de Pitch (Slides 15 min) & Préparation Q&A.
