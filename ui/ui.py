from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer, Static

from metrics.metrics import get_metrics

class MetricsWidget(Static):
    
    async def on_mount(self) -> None:
        self.set_interval(.5, self.refresh_metrics)

    async def refresh_metrics(self) -> None:
        metrics = get_metrics()

        """ metrics map
        return {
        "cpu_percent": cpu_percent,
        "mem_percent": mem_percent,
        "bytes_sent": bytes_sent,
        "bytes_rec": bytes_rec
    }
        """

        text = (
            f"[bold white]CPU Usage: [/bold white] {metrics['cpu_percent']}%\n"
            f"[bold white]MEM Usage: [/bold white] {metrics['mem_percent']}%\n"
            f"[bold white]Bytes Sent: [/bold white] {metrics['bytes_sent']}\n"
            f"[bold white]Bytes Received: [/bold white] {metrics['bytes_rec']}\n"
        )
        self.update(text)

class MonitorApp(App):

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        # The container below holds our live metrics widget.
        yield Container(MetricsWidget(), id="main")
        yield Footer()