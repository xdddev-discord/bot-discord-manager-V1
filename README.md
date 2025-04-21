# 📦 Manager Bot V1

Ce projet est un bot Discord développé avec **discord.py**, organisé en **Cogs** pour une structure claire et évolutive.
Ceci n'est que la V1 et la V2 sera au top pour gérer et personnaliser ton serveur rapidement.

## 🔧 Installation

1. **Cloner le repo**

```bash
git clone https://github.com/xdddev-discord/bot-discord-manager-V1
```

2. **Installer les discord.py**

Pour que le bot fonctionne il faut **discord.py** installé
```bash
pip install discord.py
```



4. **Configurer le bot**

Modifier le fichier `config.json` :

```json
{
  "token": "TON_TOKEN",
  "prefix": "!+",
  "developper": "your_id",
  "version": "1.0.0",
  ...
}
```

> 💡 Assure-toi que le token est bien celui de ton bot, et que les ID sont valides.

## 🚀 Lancer le bot

```bash
python main.py
```

## 📁 Structure du projet

```
.
├── main.py               
├── cogs/                 
│   ├── vcpv.py           
│   ├── lock.py          
│   ├── privacy.py        
│   ├── clear.py          
│   ├── help.py           
│   └── commands_config.py 
├── config.json          
├── utils/
│   └── io_utils.py       
```

## 🛠 Fonctions principales

- `vcpv <action> <id si néccessaire>` → Création / suppression / gestion de salons vocaux persos
- `lock`, `unlock` → Contrôle de l'accès aux salons texte
- `pv`, `unpv` → Rendre un salon privé ou public
- `clear` → Nettoyage de messages avec limite configurée
- `help` → Système d'aide avec embed + navigation
- `/addcommand`, `/removecommand` → Gestion dynamique du help

## Crédits

- [discord.py](https://github.com/Rapptz/discord.py)
- Ton imagination ✨

---

Prêt à faire tourner ton bot sur ton serveur !


