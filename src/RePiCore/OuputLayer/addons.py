DEFAULT_CSS = """
<style>
    .root{
        background: rgb(120, 120, 120);
    }
    .NEUTRAL {
        padding: 5px;
        border-radius: 5px;
        background: rgba(0,100,255,0.7);
    }
    .FAIL {
        padding: 5px;
        border-radius: 5px;
        background: rgba(255,0,0,0.7);
    }
    .PASS {
        padding: 5px;
        border-radius: 5px;
        background: rgba(0,255,0,0.7);
    }
    .table_container{
        background: rgb(200, 200, 200);
        max-width: 60vw;
        max-height: 40vh;
        padding: 15px;
    }
    .graph_container{
        background: rgb(200, 200, 200);
        max-width: 80vw;
        max-height: 30vh;
        padding: 15px;
    }
</style>
"""

DEFAULT_JS = """

"""

HEAD_INCLUDE = """
<script src="https://cdn.plot.ly/plotly-2.24.1.min.js" charset="utf-8"></script>
"""
