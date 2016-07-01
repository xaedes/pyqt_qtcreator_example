
.PHONY: ui clean

ui: form_ui.py

%_ui.py: %.ui
	pyuic4 $< > $@
	
clean:
	-rm *.pyc
	-rm *_ui.py
	