DEFAULT_CSS = """
<style>
    :root {
        --border-color: #132238;
        --hover-color: #cefdfd;
        --header-color: #cefdfd;
        --container-color: #c6e9f0;
        --background-color: #ebf0f6;

        --neutral-status: rgba(0,100,255,0.7);
        --fail-status: rgba(255,0,0,0.7);
        --pass-status: rgba(0,255,0,0.7);

        font-size: 12;
        font-family: 'Lucida Console';
        padding: 20px
    }
    html {
        background: var(--background-color);
    }
    .NEUTRAL {
        padding: 4px;
        border-radius: 4px;
        background: var(--neutral-status);
    }
    .FAIL {
        padding: 4px;
        border-radius: 4px;
        background: var(--fail-status);
    }
    .PASS {
        padding: 4px;
        border-radius: 4px;
        background: var(--pass-status);
    }
    .table_container{
        margin-top: 10px;
        max-width: 50vw;
        max-height: 50vh;
    }
    .graph_container{
        padding: 10px;
        margin-top: 10px;
        background: var(--container-color);
        max-width: 50vw;
        max-height: 50vh;
        border-radius: 7px;
        border-style: solid;
        border-color: var(--border-color);
        border-radius: 7px;
    }
    table {
        background: var(--container-color);
        padding: 10px;
        border-radius: 7px;
        border-style: solid;
        border-color: var(--border-color);
    }
    th, td {
        padding: 3px;
        border-width: 0;
        border-bottom: 1px solid var(--border-color);
    }
    th {
        background: var(--header-color);
    }
    tr:hover {
        border-width: 0;
        background: var(--hover-color);
        font-weight: bold;
    }
    p {
        border-radius: 5px;
        padding: 5px;
        width: min;
        border-style: solid;
        border-color: var(--background-color);
        margin: 1px;
    }
    p:hover {
        background: var(--hover-color);
        border-color: var(--border-color);
    }
</style>
"""

DEFAULT_JS = """

"""

HEAD_INCLUDE = """
<script src="https://cdn.plot.ly/plotly-2.24.1.min.js" charset="utf-8"></script>
"""
