DEFAULT_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{TITLE}}</title>
    {{CSS}}
    {{JS}}
    {{HEAD_INCLUDE}}
</head>
<body>
    {% for RE in REPORT_ELEMENTS %}
        {{RE}}
    {% endfor %}
</body>
</html>
"""
