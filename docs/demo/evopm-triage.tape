Output docs/demo/evopm-triage.gif
Output docs/demo/evopm-triage.mp4

Require python

Set Shell "bash"
Set FontSize 18
Set Width 1200
Set Height 900
Set Padding 24
Set Theme "Catppuccin Mocha"
Set TypingSpeed 28ms
Set Framerate 30

Type "clear" Enter
Sleep 1s

Type "echo 'Do I need a multi-agent system for this task?'" Enter
Sleep 2s

Type "PYTHONPATH=src python -m evopm triage examples/quarterly-report.json" Enter
Sleep 8s

Type "echo 'Make the architecture decision before building the architecture.'" Enter
Sleep 4s
