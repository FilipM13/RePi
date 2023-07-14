PLAIN = """
<{{object.tag}}>{{object.text}}</{{object.tag}}>
"""

WITHCHECK = """
<p title="{{object.description}}">
    {{object.name}}: <span class="{{object.status.name}}">
        {{object.checked_value}}
    </span>
</p>
"""

TABLE = """
<div class="table_container">
    {{TABLE}}
</div>
"""

HISTOGRAM = """
<div id="{{object.id}}" class="graph_container"></div>
<script>
    target = document.getElementById('{{object.id}}');

    data = [
    {% set series = object.series %}
    {% for ser in series %}
        {
            x: [ser.x],
            name: "ser.name",
            type: "histogram",
            {% if 'color' in ser %} color: rgba{{ser.color}}{% endif %}
        },
    {% endfor %}
    ]

    layout = {
        barmode: "overlay"
    }

    Plotly.newPlot(target, data, layout);
</script>
"""

SCATTERPLOT = """
<div id="{{object.id}}" class="graph_container"></div>
<script>
    target = document.getElementById('{{object.id}}');

    data = [
    {% for ser in object.series %}
        {
            x: ser.x,
            y: ser.y,
            name: "ser.name",
            mode: "markers",
            type: "scatter",
            {% if 'color' in ser %} color: rgba{{ser.color}}{% endif %}
        },
    {% endfor %}
    ]

    Plotly.newPlot(target, data);
</script>
"""
