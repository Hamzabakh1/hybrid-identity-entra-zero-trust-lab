# 30 questions techniques — Identité hybride

Statut : préparation d’entretien. Les commandes tenant/serveur sont des exemples non exécutés; seuls les tests hors ligne du rapport de validation ont été exécutés.

## 1. Que synchronise Entra Connect ?

**Question du jury :** Que synchronise Entra Connect ?

**Réponse technique :** Des objets et attributs AD sélectionnés vers Entra selon les règles configurées.

**Explication détaillée :** Synchronisation et authentification sont des fonctions différentes.

**Exemple pratique :** Pilote sur OU Engineering.

**Commandes pertinentes :** `Get-ADUser -SearchBase <OU> -Filter *`

**Pièges à éviter :** Activer toute la forêt sans pilote.

**Question de relance possible :** Comment contrôler les exclusions ?

## 2. Pourquoi un source anchor ?

**Question du jury :** Pourquoi un source anchor ?

**Réponse technique :** Il lie durablement objet AD et objet cloud.

**Explication détaillée :** Changer cet identifiant sans plan peut créer doublons ou mauvais appariement.

**Exemple pratique :** Suivre un compte synthétique avant/après renommage.

**Commandes pertinentes :** `Get-MgUser -UserId <id> -Property OnPremisesImmutableId`

**Pièges à éviter :** Utiliser seulement le display name.

**Question de relance possible :** Que faire lors d’une migration forêt ?

## 3. Connect Sync ou Cloud Sync ?

**Question du jury :** Connect Sync ou Cloud Sync ?

**Réponse technique :** Choisir selon fonctionnalités, topologie, HA et prérequis actuels.

**Explication détaillée :** Cloud Sync emploie des agents et certaines fonctions diffèrent de Connect Sync.

**Exemple pratique :** Comparer besoins d’écriture et règles de filtrage.

**Commandes pertinentes :** `Get-ADSyncScheduler`

**Pièges à éviter :** Les déployer en écriture sur la même portée.

**Question de relance possible :** Quel cas impose Connect Sync ?

## 4. Que requiert SYNC01 ?

**Question du jury :** Que requiert SYNC01 ?

**Réponse technique :** Serveur supporté joint au domaine, accès AD et sortie TLS vers le tenant.

**Explication détaillée :** Le serveur traite des secrets et appartient au niveau de sécurité tier 0.

**Exemple pratique :** Isoler SYNC01 du réseau poste.

**Commandes pertinentes :** `Test-NetConnection <dc> -Port 389`

**Pièges à éviter :** L’installer sur CLIENT01.

**Question de relance possible :** Comment protéger les comptes de sync ?

## 5. Pourquoi `.test` pose problème cloud ?

**Question du jury :** Pourquoi `.test` pose problème cloud ?

**Réponse technique :** Le suffixe ne peut pas être vérifié comme domaine Internet possédé.

**Explication détaillée :** Un UPN de connexion réel doit être mappé vers un domaine vérifié.

**Exemple pratique :** lab.amal@corp.example.test devient UPN de test possédé.

**Commandes pertinentes :** `Get-ADUser lab.amal.atlas -Properties UserPrincipalName`

**Pièges à éviter :** Supposer une connexion M365 avec `.test`.

**Question de relance possible :** Comment gérer un UPN alternate ?

## 6. PHS, PTA ou fédération ?

**Question du jury :** PHS, PTA ou fédération ?

**Réponse technique :** PHS simplifie la disponibilité; PTA dépend d’agents; fédération ajoute un IdP.

**Explication détaillée :** Le choix doit équilibrer exigences de contrôle, risque de panne et exploitation.

**Exemple pratique :** Sélectionner PHS pour un pilote sans exigence fédérée.

**Commandes pertinentes :** `Get-MgDomainFederationConfiguration`

**Pièges à éviter :** Confondre PHS avec mot de passe en clair dans le cloud.

**Question de relance possible :** Quelle dépendance d’authentification existe en panne WAN ?

## 7. Que signifie Seamless SSO ?

**Question du jury :** Que signifie Seamless SSO ?

**Réponse technique :** Réduit les invites sur postes du domaine dans certaines conditions.

**Explication détaillée :** Il ne remplace pas MFA ni la vérification du flux d’authentification.

**Exemple pratique :** CLIENT01 accède à M365 après configuration validée.

**Commandes pertinentes :** `klist`

**Pièges à éviter :** Affirmer que sync seule donne le SSO.

**Question de relance possible :** Quelles limites navigateur ?

## 8. Comment diagnostiquer un objet absent ?

**Question du jury :** Comment diagnostiquer un objet absent ?

**Réponse technique :** Contrôler OU, filtre, attributs, connecteur, export et erreurs.

**Explication détaillée :** La recherche doit suivre l’objet depuis AD jusqu’au tenant.

**Exemple pratique :** Utilisateur Finance hors portée pilote.

**Commandes pertinentes :** `Get-ADUser <id>; Get-MgUser -Filter <filter>`

**Pièges à éviter :** Relancer tous les cycles sans voir l’erreur.

**Question de relance possible :** Comment éviter un doublon ?

## 9. Comment traiter un UPN dupliqué ?

**Question du jury :** Comment traiter un UPN dupliqué ?

**Réponse technique :** Trouver l’autorité de chaque objet, corriger la collision puis relancer.

**Explication détaillée :** Modifier le mauvais objet peut casser l’identité déjà utilisée.

**Exemple pratique :** Deux comptes synthétiques portent la même adresse.

**Commandes pertinentes :** `Get-ADUser -LDAPFilter <filter>`

**Pièges à éviter :** Supprimer l’objet cloud sans analyse.

**Question de relance possible :** Quel autre attribut doit être unique ?

## 10. Pourquoi commencer CA en report-only ?

**Question du jury :** Pourquoi commencer CA en report-only ?

**Réponse technique :** Mesurer l’impact sans appliquer le contrôle d’accès.

**Explication détaillée :** Les logs indiquent le résultat hypothétique; aucun MFA n’est exigé par cette politique seule.

**Exemple pratique :** Politique pilote sur groupe lab.

**Commandes pertinentes :** `Get-MgIdentityConditionalAccessPolicy`

**Pièges à éviter :** Interpréter report-only comme protection active.

**Question de relance possible :** Quelles limites de report-only ?

## 11. Quel rôle des comptes d’urgence ?

**Question du jury :** Quel rôle des comptes d’urgence ?

**Réponse technique :** Maintenir un chemin d’administration indépendant et surveillé.

**Explication détaillée :** Une politique restrictive appliquée sans exclusion peut verrouiller le tenant.

**Exemple pratique :** Deux comptes dédiés exclus d’une CA bloquante.

**Commandes pertinentes :** `Get-MgIdentityConditionalAccessPolicy`

**Pièges à éviter :** Les associer à un téléphone personnel unique.

**Question de relance possible :** À quelle fréquence les tester ?

## 12. Quelle licence pour Conditional Access ?

**Question du jury :** Quelle licence pour Conditional Access ?

**Réponse technique :** Vérifier une licence Entra ID P1 ou offre qui l’inclut.

**Explication détaillée :** Les fonctions risque/PIM peuvent requérir P2 selon le cas.

**Exemple pratique :** Contrôler entitlements avant le pilote.

**Commandes pertinentes :** `Get-MgSubscribedSku`

**Pièges à éviter :** Présumer qu’un tenant gratuit suffit.

**Question de relance possible :** Quelle différence P1/P2 ?

## 13. Comment enregistrer MFA sans verrouillage ?

**Question du jury :** Comment enregistrer MFA sans verrouillage ?

**Réponse technique :** Piloter méthodes, récupération et comptes d’urgence avant enforcement.

**Explication détaillée :** Les méthodes doivent répondre aux risques et rester récupérables.

**Exemple pratique :** Groupe lab avec méthode résistante au phishing.

**Commandes pertinentes :** `Get-MgUserAuthenticationMethod`

**Pièges à éviter :** Forcer MFA à tous en une étape.

**Question de relance possible :** Comment traiter une perte de méthode ?

## 14. Qu’est-ce que PIM ?

**Question du jury :** Qu’est-ce que PIM ?

**Réponse technique :** Gestion d’activation temporaire de privilèges avec contrôles.

**Explication détaillée :** Éligibilité, justification et approbation réduisent les privilèges permanents.

**Exemple pratique :** Admin lab active un rôle pour une intervention.

**Commandes pertinentes :** `Get-MgRoleManagementDirectoryRoleEligibilitySchedule`

**Pièges à éviter :** Dire qu’un rôle éligible est toujours actif.

**Question de relance possible :** Quelle licence est nécessaire ?

## 15. Comment limiter Graph PowerShell ?

**Question du jury :** Comment limiter Graph PowerShell ?

**Réponse technique :** Vérifier tenant et scopes puis utiliser les permissions minimales.

**Explication détaillée :** Une session Graph peut viser le mauvais tenant ou disposer de droits étendus.

**Exemple pratique :** Lecture ciblée des identités lab.

**Commandes pertinentes :** `Get-MgContext; Connect-MgGraph -Scopes User.Read.All`

**Pièges à éviter :** Accepter Directory.ReadWrite.All par défaut.

**Question de relance possible :** Comment utiliser app-only sans secret en clair ?

## 16. Quelle différence rôle Entra et groupe ?

**Question du jury :** Quelle différence rôle Entra et groupe ?

**Réponse technique :** Le rôle donne des droits d’administration; le groupe porte accès et ciblage.

**Explication détaillée :** L’appartenance à un groupe métier ne doit pas créer un admin global.

**Exemple pratique :** Finance-Users pour application, admin dédié pour tenant.

**Commandes pertinentes :** `Get-MgDirectoryRole; Get-MgGroup`

**Pièges à éviter :** Mettre tout IT en Global Administrator.

**Question de relance possible :** Comment réaliser une revue des rôles ?

## 17. Comment réaliser un joiner ?

**Question du jury :** Comment réaliser un joiner ?

**Réponse technique :** Créer à la source, attribuer accès minimal, synchroniser et vérifier la connexion.

**Explication détaillée :** La demande RH et les approbations précèdent les changements techniques.

**Exemple pratique :** lab.amal passe planned à active dans le plan.

**Commandes pertinentes :** `python scripts/automation/lifecycle.py --action join ...`

**Pièges à éviter :** Donner les droits avant date d’entrée.

**Question de relance possible :** Quel identifiant de corrélation conserver ?

## 18. Comment réaliser un mover ?

**Question du jury :** Comment réaliser un mover ?

**Réponse technique :** Retirer droits anciens puis attribuer droits nouveaux après approbation.

**Explication détaillée :** L’accumulation de rôles est un risque fréquent de mobilité interne.

**Exemple pratique :** Finance vers Operations, revue des accès.

**Commandes pertinentes :** `python scripts/automation/lifecycle.py --action move ...`

**Pièges à éviter :** Ajouter nouveau groupe sans retirer ancien.

**Question de relance possible :** Quels accès non groupés rechercher ?

## 19. Comment réaliser un leaver ?

**Question du jury :** Comment réaliser un leaver ?

**Réponse technique :** Désactiver source, révoquer sessions et licences selon politique, vérifier refus.

**Explication détaillée :** Le délai de token et de sync peut laisser une fenêtre d’accès.

**Exemple pratique :** lab.nora passe active à disabled.

**Commandes pertinentes :** `Revoke-MgUserSignInSession -UserId <id>`

**Pièges à éviter :** Supprimer immédiatement les données légales.

**Question de relance possible :** Comment mesurer le délai de révocation ?

## 20. Où analyser un échec de connexion ?

**Question du jury :** Où analyser un échec de connexion ?

**Réponse technique :** Sign-in logs, code erreur, application, CA, méthode, appareil et correlation ID.

**Explication détaillée :** Un échec de connexion ne prouve pas un défaut de sync.

**Exemple pratique :** Comparer état cloud de lab.amal et log UTC.

**Commandes pertinentes :** `Get-MgAuditLogSignIn -Filter <filter>`

**Pièges à éviter :** Tester à l’aveugle en réinitialisant le mot de passe.

**Question de relance possible :** Comment relier un log à une politique CA ?

## 21. Quel rôle des audit logs ?

**Question du jury :** Quel rôle des audit logs ?

**Réponse technique :** Ils tracent les changements d’objets et politiques.

**Explication détaillée :** Conserver UTC, acteur, cible et corrélation aide l’enquête et la conformité.

**Exemple pratique :** Modification groupe Finance après mover.

**Commandes pertinentes :** `Get-MgAuditLogDirectoryAudit`

**Pièges à éviter :** Ne garder qu’une capture d’écran.

**Question de relance possible :** Quelle rétention est disponible ?

## 22. Comment protéger SYNC01 ?

**Question du jury :** Comment protéger SYNC01 ?

**Réponse technique :** Durcir OS, comptes, réseau, sauvegarde et supervision du serveur tier 0.

**Explication détaillée :** Sa compromission peut altérer l’identité cloud.

**Exemple pratique :** Admin du poste CLIENT01 ne peut y accéder.

**Commandes pertinentes :** `Get-LocalGroupMember Administrators`

**Pièges à éviter :** Le traiter comme simple serveur applicatif.

**Question de relance possible :** Comment isoler ses identifiants ?

## 23. Que faire si sync s’arrête ?

**Question du jury :** Que faire si sync s’arrête ?

**Réponse technique :** Examiner service/agent, connectivité, export et dernières erreurs avant relance.

**Explication détaillée :** Un arrêt prolongé fausse le cycle de vie, mais les connexions existantes peuvent encore fonctionner selon méthode.

**Exemple pratique :** Agent SYNC01 indisponible.

**Commandes pertinentes :** `Get-Service ADSync; Get-ADSyncScheduler`

**Pièges à éviter :** Recréer les utilisateurs cloud manuellement.

**Question de relance possible :** Comment reprendre sans doublon ?

## 24. Comment éviter un lockout CA ?

**Question du jury :** Comment éviter un lockout CA ?

**Réponse technique :** Scope pilote, report-only, What If, emergency access et retour arrière.

**Explication détaillée :** Le résultat report-only ne vaut pas enforcement; tester comptes et appareils variés.

**Exemple pratique :** Politique ciblant groupe lab seulement.

**Commandes pertinentes :** `Get-MgIdentityConditionalAccessPolicy`

**Pièges à éviter :** Activer pour All users d’emblée.

**Question de relance possible :** Comment récupérer si tous les admins sont bloqués ?

## 25. Que veut dire Zero Trust ici ?

**Question du jury :** Que veut dire Zero Trust ici ?

**Réponse technique :** Vérifier explicitement, limiter privilèges et supposer une compromission.

**Explication détaillée :** C’est une architecture de décisions et signaux, pas un produit unique.

**Exemple pratique :** CA + MFA + revue accès + logs.

**Commandes pertinentes :** `Get-MgAuditLogSignIn`

**Pièges à éviter :** Dire que MFA suffit à elle seule.

**Question de relance possible :** Quels signaux de risque intégrer ?

## 26. Comment gouverner les accès ?

**Question du jury :** Comment gouverner les accès ?

**Réponse technique :** Définir propriétaires, revues périodiques et retrait automatique justifié.

**Explication détaillée :** L’accès de projet doit expirer ou être réapprouvé.

**Exemple pratique :** Revue trimestrielle du groupe Engineering.

**Commandes pertinentes :** `Get-MgGroupMember`

**Pièges à éviter :** Laisser des groupes sans propriétaire.

**Question de relance possible :** Quel indicateur d’orphelins suivre ?

## 27. Quelle réponse à un compte compromis ?

**Question du jury :** Quelle réponse à un compte compromis ?

**Réponse technique :** Contenir, révoquer sessions, examiner logs/permissions et restaurer proprement.

**Explication détaillée :** Le traitement doit préserver les preuves et rechercher la cause racine.

**Exemple pratique :** lab.salma présente une connexion anormale.

**Commandes pertinentes :** `Revoke-MgUserSignInSession -UserId <id>`

**Pièges à éviter :** Effacer les logs en supprimant l’objet.

**Question de relance possible :** Quand réactiver le compte ?

## 28. Pourquoi un objet cloud peut rester actif après leave ?

**Question du jury :** Pourquoi un objet cloud peut rester actif après leave ?

**Réponse technique :** Sync retardée, scope erreur ou état source non propagé.

**Explication détaillée :** Il faut comparer état AD, export et cloud; révoquer la session indépendamment.

**Exemple pratique :** lab.nora désactivée dans AD mais encore enabled cloud.

**Commandes pertinentes :** `Get-MgUser -UserId <id> -Property AccountEnabled`

**Pièges à éviter :** Attendre simplement le prochain cycle.

**Question de relance possible :** Comment prouver la fermeture d’accès ?

## 29. Comment valider l’authentification hybride ?

**Question du jury :** Comment valider l’authentification hybride ?

**Réponse technique :** Tester identité, méthode, CA et application avec une connexion synthétique.

**Explication détaillée :** La présence d’objet Entra ne prouve pas l’authentification ou autorisation.

**Exemple pratique :** lab.amal se connecte à une app pilote.

**Commandes pertinentes :** `Get-MgAuditLogSignIn -Filter <filter>`

**Pièges à éviter :** Montrer seulement le portail utilisateurs.

**Question de relance possible :** Quels résultats log attendus ?

## 30. Quelle preuve présenter au jury ?

**Question du jury :** Quelle preuve présenter au jury ?

**Réponse technique :** Plan JML et tests locaux, puis préciser tenant et sync non exécutés.

**Explication détaillée :** Les résultats doivent porter environnement, timestamp et source réelle.

**Exemple pratique :** Montrer le rapport unittest et l’architecture.

**Commandes pertinentes :** `python -m unittest discover -s tests -v`

**Pièges à éviter :** Présenter une transition simulée comme déprovisionnement réel.

**Question de relance possible :** Quelle étape débloque la preuve cloud ?
