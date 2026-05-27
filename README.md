# Agent Mail — Les Clés de l'Atelier

## Déploiement Render.com

1. Créer un repo GitHub avec ces fichiers
2. Render → New → Web Service → connecter le repo
3. Environment Variables : `ANTHROPIC_API_KEY` = votre clé
4. Build Command : `pip install -r requirements.txt`
5. Start Command : `gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120`
6. Deploy → URL partageable aux collaborateurs
