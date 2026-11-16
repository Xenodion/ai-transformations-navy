# Les 10 initiatives expliquées simplement, et les 4 cas phares en détail

**Usage :** fiche de révision en français pour comprendre et expliquer le portefeuille à l'oral. Sources : rapport complet (§3 et §4), deck (slides 8–11, 23, 27), workbook. Les montants sont en $m sauf P13 (€m, converti à 1.1165 $/€). Tout bénéfice est une **hypothèse**, pas un chiffre TotalEnergies.

**Idée commune aux 10 cas :** TotalEnergies a déjà les plateformes (plus de 10 000 modèles IA, ~100 solutions Digital Factory, AspenTech, Cognite). Chaque cas prend une solution existante et la **transforme en cash mesuré**, avec un trio dédié (data scientist du Digital Factory + data engineer de la branche + expert métier), un sponsor de branche, une baseline signée par la Finance et un arrêt automatique si les seuils ne sont pas atteints.

---

## Partie A. Les 10 initiatives, une par une

Réponse à « la liste n'est nulle part » : elle existe dans le rapport (§3, tableau « Portfolio and investment priorities », avec seulement une ligne de « mécanisme de valeur » en jargon) ; le deck n'en montre que la répartition par horizon (slide 8) et les cas complémentaires en appendice (slide 27). **Il n'y avait pas d'explication en langage simple**, d'où cette fiche. Les numéros sautent (P06, P07, P10, P11…) car ces idées de la longue liste ont été écartées ; les raisons sont dans `work/archive/`.

Horizons : **H1** = améliorer l'existant, retour rapide ; **H2** = redessiner un flux de travail transverse ; **H3** = option vers un nouveau modèle économique.

Total du portefeuille : **$9.82m d'investissement ponctuel** (dont $5.69m de capex et $4.12m de charges de lancement), **$12.12m de coûts récurrents**, soit **$21.94m** sur Y0–Y5.

### P01. Maintenance prédictive du raffinage (cas phare)
- **Horizon :** H1.
- **Investissement ponctuel :** $1.40m. **Coût brut Y0–Y5 :** $3.15m.
- **En une phrase :** détecter à l'avance les pannes de machines tournantes sur 2 raffineries pour éviter des arrêts et des réparations d'urgence.
- **Valeur :** barils supplémentaires vendus + réparations évitées = **$1.87m par an**.
- **Calcul :** 250 000 b/j × 365 × 0.45 % × 70 % vendus × $6/baril + $0.15m de réparations.
- **Détail complet :** Partie B.

### P02. Surveillance de la production amont
- **Horizon :** H1.
- **Investissement ponctuel :** $0.90m. **Coût brut Y0–Y5 :** $2.23m.
- **En une phrase :** repérer plus vite les pertes de production sur 2 hubs pétroliers pour récupérer des barils.
- **Valeur :** environ **$1.48m par an** (calcul fait à partir de la formule du rapport).
- **Calcul :** 2 hubs × 135 b/j récupérés × 365 jours × $15 de marge par baril.
- **Dépendance :** accès aux données de production et événements distincts de ceux de P03.
- **Point d'attention :** cas complémentaire, estimation légère ; baseline signée par le propriétaire métier avant tout engagement.

### P03. Conseil au forage en eaux profondes (cas phare)
- **Horizon :** H2.
- **Investissement ponctuel :** $1.40m. **Coût brut Y0–Y5 :** $3.65m.
- **En une phrase :** aide à la planification des puits sur 2 rigs opérés pour réduire les jours de forage, à condition que le contrat baisse la facture.
- **Valeur :** **$2.88m par an**.
- **Calcul :** 2 rigs × 6 jours évitables × $0.40m par jour × 60 % réalisables.
- **Détail complet :** Partie B.

### P04. Performance du parc renouvelable
- **Horizon :** H1.
- **Investissement ponctuel :** $1.40m. **Coût brut Y0–Y5 :** $2.70m.
- **En une phrase :** résoudre plus tôt les pannes d'éoliennes et de centrales solaires pour produire et vendre plus d'électricité.
- **Valeur :** **$1.60m par an** à pleine échelle ; NPV de base +$1.05m, retour en 3.1 ans (4.3 ans en downside).
- **Calcul :** 3 000 MW (périmètre illustratif) × 8 760 h × 30 % de facteur de charge × 0.45 % récupéré × $45/MWh.
- **Dépendance :** bases de référence du centre O3C et du fabricant, droit de vendre l'électricité récupérée.

### P05. Copilot et gestion des licences
- **Horizon :** H1.
- **Investissement ponctuel :** $0.30m. **Coût brut Y0–Y5 :** $0.73m.
- **En une phrase :** résilier les licences Copilot redondantes ou inutilisées.
- **Valeur :** environ **$0.43m par an**.
- **Calcul :** 10 000 licences × 12 % résiliables × $30 par mois × 12.
- **Dépendance :** droits de résiliation vérifiés par les achats, alternatives pour les utilisateurs.
- **Point d'attention :** le cas le plus simple et le moins risqué du portefeuille.

### P08. Rétention client
- **Horizon :** H1.
- **Investissement ponctuel :** $1.50m. **Coût brut Y0–Y5 :** $2.95m.
- **En une phrase :** cibler les clients électricité et gaz susceptibles de partir avec des gestes adaptés, pour en garder plus.
- **Valeur :** **$1.62m par an** ; NPV de base +$0.99m, retour en 3.2 ans (4.5 ans en downside).
- **Calcul :** 1.2 million de comptes × 10 % de churn × 9 % de réduction relative × $150 de contribution annuelle, nette des incitations.
- **Dépendance :** accès au CRM, confidentialité des données, groupe témoin pour prouver que la rétention est incrémentale.

### P09. Optimisation des voyages GNL
- **Horizon :** H2.
- **Investissement ponctuel :** $0.50m. **Coût brut Y0–Y5 :** $1.04m.
- **En une phrase :** mieux planifier les routes des méthaniers que TotalEnergies contrôle pour consommer moins de carburant.
- **Valeur :** environ **$0.60m par an**.
- **Calcul :** 30 voyages × $1m de carburant contrôlable × 2 % d'amélioration.
- **Dépendance :** droits de charter, baseline de routage, factures de carburant.

### P12. Licence technologique e-SAF (cas phare)
- **Horizon :** H3.
- **Investissement ponctuel :** $1.00m. **Coût brut Y0–Y5 :** $2.85m.
- **En une phrase :** utiliser l'IA pour trouver plus vite des catalyseurs, et en faire un paquet technologique licencié à des développeurs tiers.
- **Valeur :** redevances de tiers **conditionnelles** : $0.60m en Y3, $1.50m en Y4, $2.30m en Y5, non signées.
- **Détail complet :** Partie B.

### P13. Retail : demande et démarques (cas phare)
- **Horizon :** H1.
- **Investissement ponctuel :** $1.12m (€1.0m). **Coût brut Y0–Y5 :** $1.70m (€1.52m).
- **En une phrase :** prévoir la demande de 100 stations françaises et ajuster prix et stocks pour réduire gaspillage et ruptures.
- **Valeur :** **€0.635m par an** = gaspillage €0.245m + démarques €0.250m + ruptures €0.140m.
- **Détail complet :** Partie B.

### E01. Valeur partagée et contrôles
- **Horizon :** H1 (cas support, pas de cas métier).
- **Investissement ponctuel :** $0.30m. **Coût brut Y0–Y5 :** $0.94m.
- **En une phrase :** un registre des modèles et des baselines, qui dit qui possède quoi et quel bénéfice est validé par la Finance.
- **Valeur :** **aucun bénéfice propre** ; c'est un coût de contrôle financé une seule fois, dont dépendent les gates de tous les autres cas. Sa NPV isolée est de −$0.76m.
- **Point d'attention :** il est exclu du scénario « moitié du budget », qui « s'appuie sur les contrôles existants ».

### Rôle de chaque groupe
- **Cas phares (4) :** P01, P03, P12, P13. Cas détaillés, avec cash-flows par scénario.
- **Cas complémentaires (5) :** P02, P04, P05, P08, P09. Même méthode, estimations plus légères ; libérés seulement après baseline signée.
- **Cas support (1) :** E01.

**Idée commune :** TotalEnergies a déjà les plateformes (plus de 10 000 modèles IA, ~100 solutions Digital Factory, AspenTech, Cognite). Chaque cas transforme une solution existante en **cash mesuré**, avec un trio dédié, un sponsor de branche, une baseline signée par la Finance et un arrêt automatique si les seuils ne sont pas atteints.

---

## Partie B. Les 4 cas phares

### P01. Maintenance prédictive du raffinage (H1)

**Le problème, en simple.** Une pompe ou un compresseur qui tombe en panne sans prévenir arrête une unité : on perd de la production vendable et on paie une réparation d'urgence. Des capteurs et un modèle peuvent signaler « cette machine va lâcher dans X jours », ce qui permet de la réparer pendant un arrêt planifié.

**Ce qu'on finance.** Un pilote sur les machines tournantes critiques de **deux raffineries** (périmètre supposé). On achète un outil de maintenance prédictive du marché et on le branche sur la plateforme AspenTech déjà en déploiement et sur le processus de maintenance existant. Un ingénieur fiabilité valide chaque alerte ; aucun modèle ne déclenche d'arrêt automatique.

**D'où vient l'argent (calcul).**
250 000 b/j × 365 jours × 0.45 % de débit récupéré × 70 % effectivement vendu × $6 de marge/baril = **$1.72m**, plus **$0.15m** de réparations d'urgence évitées = **$1.87m par an** en régime de croisière.
En clair : 0.45 % de 250 kb/j, soit environ 1 125 barils de plus par jour.

**Coûts.** Investissement $1.4m : $1.0m de matériel et logiciel (capex, $0.5m en Y0 et $0.5m en Y1) + $0.4m de mise en œuvre et formation en Y1. Récurrent : $0.20m, 0.35, 0.40, 0.40, 0.40 en Y1–Y5. Coût brut total **$3.15m**. Les bénéfices montent par paliers : 20 %, 60 %, 85 %, 100 %, 100 %.

**Chiffres clés.** NPV **+$1.62m** à 9.5 %, IRR **47.6 %**, retour sur investissement en **2.6 ans** (3.7 ans en downside). Seuil d'équilibre : $1.08m/an, soit **57.6 %** du bénéfice modélisé. Autrement dit, le bénéfice peut chuter de 42 % avant que la NPV passe à zéro.

**Hypothèse la plus faible.** Le gain de débit (0.45 %), la part vendue (70 %) et la marge ($6/baril) sont des hypothèses, pas des mesures de sites. Une bonne prédiction ne vaut rien en soi : on ne compte que le baril vendu et la facture évitée.

**Gate et arrêt.** Avant le pilote : baseline de production et de maintenance, droits sur les données. Mois 12 (sponsor raffinage + Finance) : pilote sûr, chaîne alerte → action → baril vendu vérifiée, au moins 60 % des décisions prises dans l'outil, NPV prospective > 0 à 9.5 %. Pause immédiate sur tout incident de sécurité.

**Pourquoi c'est un H1.** On optimise un actif existant avec une famille d'outils éprouvée, sans nouveau data lake.

**Comment l'expliquer en 30 secondes.** « On évite des pannes de machines dans deux raffineries. Les barils qu'on aurait perdus sont vendus et les réparations d'urgence disparaissent. Le cas reste positif même si on obtient seulement 58 % du bénéfice prévu, et on ne compte que ce que la Finance peut vérifier sur une facture ou un baril vendu. »

**Questions probables.**
- *« Pourquoi $6 le baril ? »* Hypothèse prudente : le marqueur de marge de raffinage était à $33.2/b au T3 2026, mais c'est un indice de marché, pas notre marge réalisée ; nous ne le prenons pas.
- *« Pourquoi mes équipes ne l'ont pas déjà fait ? »* La plateforme AspenTech est encore en déploiement (jusqu'en 2027–28) ; le goulot est l'organisation du projet (quatre lignes hiérarchiques), pas l'algorithme.
- *« Equinor annonce $120m ? »* Cumulés depuis 2020, partenaires inclus : du contexte, pas une preuve.

---

### P03. Conseil au forage en eaux profondes (H2)

**Le problème, en simple.** Un rig de forage en eaux profondes coûte environ **$0.40m par jour**. Si des données de puits bien exploitées permettaient de finir une phase de forage quelques jours plus tôt, on pourrait économiser. Mais **gagner du temps n'est pas gagner de l'argent** : il faut que le contrat avec le contracteur permette de libérer le rig plus tôt ou de payer moins.

**Ce qu'on finance.** Un outil d'**aide à la décision** (pas de pilotage autonome) sur **deux rigs ou campagnes opérés** par TotalEnergies. On réutilise le déploiement Cognite existant et on achète/combine des logiciels éprouvés avec l'expertise forage maison. Les ingénieurs de forage et les équipes HSE gardent l'autorité opérationnelle et peuvent rejeter toute recommandation.

**D'où vient l'argent (calcul).**
2 rigs × 6 jours évitables par rig et par an × $0.40m par jour × 60 % = **$2.88m par an**.
Le 60 % = 80 % de part économique de TotalEnergies × 75 % d'évitabilité du paiement dans le contrat.

**Coûts.** $1.4m ponctuel : $0.8m d'intégration et logiciel (capex, $0.4m en Y0 et en Y1) + $0.6m de mise en service et formation en Y1. Récurrent : $0.30m, 0.45, 0.50, 0.50, 0.50. Coût brut **$3.65m**. Ramp-up : 0 %, 30 %, 70 %, 100 %, 100 % (aucun bénéfice en Y1).

**Chiffres clés.** NPV **+$1.86m** à 11 %, IRR **43.2 %**, retour en **3.1 ans** (3.9 en downside). Seuil d'équilibre $1.66m/an.

**Hypothèse la plus faible.** La **part économique**. À 40 % au lieu de 80 %, le bénéfice tombe à $1.44m, sous le seuil de $1.66m. D'où le **test de contrat au Gate 0, avant toute dépense Y1** : si le contrat ne permet pas de capter l'économie (libération du rig, baisse de redevances), ce périmètre est arrêté.

**Point à connaître.** Mero est opéré par Petrobras (TotalEnergies 19.3 %). Nous ne supposons donc aucun déploiement unilatéral : le périmètre est limité à des rigs que TotalEnergies opère, avec l'accord de l'opérateur, du contracteur et des partenaires.

**Pourquoi H2.** Ce n'est pas une simple optimisation : on redessine un flux de travail transverse entre ingénierie, contracteurs et finance. Valeur plus élevée, mais retour plus tardif.

**Comment l'expliquer en 30 secondes.** « Le temps gagné n'est du cash que si le contrat réduit ce qu'on paie. Avant de dépenser une seule année de budget, on teste le contrat. Si la règle de paiement ne bouge pas, on arrête ce périmètre. »

**Questions probables.**
- *« Six jours par an, c'est réaliste ? »* C'est une hypothèse volontairement modeste sur un rig qui tourne toute l'année ; le seuil d'équilibre est $1.66m, donc nous avons de la marge au cas nominal mais pas si le contrat protège le contracteur.
- *« BP a publié un exemple »* : contexte uniquement (CLM-068), aucune économie TotalEnergies n'en est déduite.

---

### P12. Licence technologique e-SAF (H3)

**Le problème, en simple.** Le carburant d'aviation durable de synthèse (e-SAF) a besoin de catalyseurs et de procédés efficaces. TotalEnergies a déjà des centres de recherche (CO2 Techno Hub, BioHub). L'idée : utiliser l'IA pour **choisir plus intelligemment les expériences** de laboratoire (plutôt qu'un plan d'expériences classique) et, si ça marche, **vendre le procédé sous licence** à des développeurs tiers d'usines e-fuel, au lieu de produire soi-même.

**Ce qu'on finance.** Une **expérience par étapes**, pas une usine : labo, données, travail de propriété intellectuelle et de commercialisation. Plafond de **$2.85m** sur 6 ans, ni démonstrateur, ni certification, ni garanties industrielles.

**D'où vient l'argent.** Redevances et frais de développement de **tiers**, non signés : **$0.60m en Y3, $1.50m en Y4, $2.30m en Y5** (total $4.4m). Aucun délai de retour n'est inventé (règle du projet pour H3).

**Coûts.** Capex $0.30m (Y0) + $0.30m (Y1) ; lancement $0.40m (Y1) ; récurrent $0.20m, 0.30, 0.40, 0.45, 0.50. Hurdle **12 %** (plus élevé : incertitude scientifique et commerciale).

**Les gates (c'est l'essentiel).**
- Avant Y0 : OneTech et le juridique confirment l'absence de doublon avec les offres et droits existants.
- Avant Y2 : au moins **deux développeurs tiers qualifiés** acceptent de discuter d'une application définie.
- Avant Y3 : **trois essais indépendants** reproduisent le résultat, analyse de liberté d'exploitation, et au moins **un développeur prêt à une évaluation payante**.
- Tout échec → arrêt des dépenses évitables, **$0.10m de clôture**.

**Chiffres clés.** Son apport à la NPV de base est faible (**+$0.18m**) : sans P12, la NPV du portefeuille est +$6.93m. En downside, P12 s'arrête après Y2 sans recette, avec $0.10m de clôture. C'est une **option** bornée, pas un moteur de rendement.

**Pourquoi H3.** Le modèle économique change : on vend une technologie à des clients externes plutôt que de produire un carburant. Si le projet n'améliorait qu'un procédé interne, il ne serait pas H3 et serait reclassé ou arrêté.

**Comment l'expliquer en 30 secondes.** « C'est notre pari à long terme, borné à moins de 3 millions et conditionné à des preuves externes : deux développeurs intéressés, des essais répétables, un développeur prêt à payer. Si une condition manque, on s'arrête pour 0.1 million. »

**Questions probables.**
- *« Le marché existe-t-il ? »* Infinium décrit un modèle de licence en Asie du Sud-Est : cela prouve une structure commerciale possible, pas une demande pour notre offre. D'où le gate sur l'intérêt des développeurs.
- *« Pourquoi seulement 10 % en H3 ? »* Option bornée ; le sous-sol est déjà financé par Mistral ; on évite de doubler.

---

### P13. Retail : demande et démarques contrôlées (H1)

**Le problème, en simple.** Dans les stations-service, les produits frais (sandwichs, viennoiseries, boissons) sont soit jetés (gaspillage), soit en rupture (ventes perdues), soit bradés trop tard. Une meilleure prévision de la demande station par station, et des **étiquettes électroniques** qui permettent de baisser un prix au bon moment, peuvent réduire ces pertes.

**Ce qu'on finance.** Un pilote dans **100 grandes stations françaises exploitées en propre** (calibration de notre initié : environ €1m pour 100 stations). On achète les étiquettes et on combine un outil de prévision avec nos données de caisse. Le gérant de station garde la main sur les prix et valide les recommandations.

**D'où vient l'argent (calcul, €0.635m par an).**
- **Gaspillage évité : €0.245m** = 100 stations × €350 000 de ventes périssables × 70 % de coût × 4 % de gaspillage de base × 25 % de réduction.
- **Démarques incrémentales : €0.250m** = 100 × 1 000 articles à risque × €2.50 de gain net.
- **Ruptures évitées : €0.140m** = 100 × €50 000 de ventes manquées × 8 % récupérés × 35 % de marge.

**Coûts.** €1.0m ponctuel : €0.8m d'étiquettes, connectivité et logiciel (capex, €0.4m en Y0 et en Y1) + €0.2m d'intégration, installation et formation (Y1). Récurrent : €0.06m en Y1, 0.10 en Y2, 0.12 en Y3–Y5. Coût brut **€1.52m (≈ $1.70m)**.

**Chiffres clés.** NPV **+€0.49m** à 9 %, IRR **30.0 %**, retour en **2.9 ans**. Downside : NPV +€0.14m, IRR 14.8 %, retour 3.8 ans ; les trois scénarios restent positifs.

**Hypothèse la plus faible.** Les **démarques doivent être incrémentales**. Sans elles, le bénéfice tombe à €0.385m, sous le seuil de €0.446m, et le cas passe sous l'équilibre. Pour cela : cohortes de produits séparées pour mesurer d'abord l'effet des démarques, essai en magasins appariés, et repli sur la prévision seule si les étiquettes ne battent pas la prévision.

**Gate et arrêt.** Mois 12 (sponsor retail + Finance) : essai en magasins appariés contre baseline, ≥60 % des décisions dans l'outil, NPV prospective > 0 à 9 %, étiquettes meilleures que la prévision seule. Sinon pas d'extension du matériel (Y2).

**Comment l'expliquer en 30 secondes.** « Moins de produits jetés, moins de ruptures, des démarques mieux placées dans 100 stations. Le point fragile est de savoir si les démarques créent de la vraie marge : on le mesure en premier, et si les étiquettes ne se justifient pas, on garde la prévision seule, moins chère. »

**Questions probables.**
- *« Pourquoi 100 stations ? »* Le calibrage de notre initié ; l'échelle mondiale de 13 000 stations n'est pas utilisée comme dénominateur.
- *« Vos chiffres viennent d'où ? »* Hypothèses locales, labellisées comme telles ; ni mesure de groupe, ni économie réalisée.

---

## Partie C. Pour tout relier

- **Un portefeuille, pas une liste de pilotes :** chaque horizon a un rôle et une règle d'arrêt. H1 (70.5 % de l'investissement ponctuel) paie vite et finance la courbe en J ; H2 (19.4 %) change des flux transverses quand les contrats permettent de capter le cash ; H3 (10.2 %) est une option bornée.
- **Le fil rouge :** « temps gagné n'est pas cash gagné ». Chaque cas nomme le mécanisme qui transforme une amélioration en euro encaissé (baril vendu, facture contractuelle baissée, vente incrémentale, licence signée) et le test qui le vérifie.
- **Les trois cas détaillés en slides** sont P13 (retail), P01 (raffinage) et P03 (forage). P12 est en appendice (slide 25).
