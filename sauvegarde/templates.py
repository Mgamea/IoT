<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Liste des sauvegardes</title>
</head>
<body>
    <h1>Liste des sauvegardes</h1>
    <ul>
        {% for sauvegarde in sauvegardes %}
            <li>{{ sauvegarde.nom }} - {{ sauvegarde.date_creation }}</li>
        {% endfor %}
    </ul>
</body>
</html>
