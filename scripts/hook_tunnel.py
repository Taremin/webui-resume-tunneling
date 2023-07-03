import os
import gradio
from modules import script_callbacks, shared

       
def before_ui():
    _default_tunnel = gradio.tunneling.Tunnel._start_tunnel
    
    def _start_tunnel(self, *args, **kwargs):
        share_token_path = shared.cmd_opts.share_token_path
        if share_token_path is not None:
            print("share token path:", os.path.abspath(share_token_path))
            if os.path.isfile(share_token_path):
                with open(share_token_path) as f:
                    self.share_token = f.read()
            else:
                with open(share_token_path, mode="w") as f:
                    f.write(self.share_token)
        return _default_tunnel(self, *args, **kwargs)

    gradio.tunneling.Tunnel._start_tunnel = _start_tunnel
    
script_callbacks.on_before_ui(before_ui)
