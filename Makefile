
.PHONY: ui clean

ui: form_ui.py

%_ui.py: %.ui
	pyuic4 $< > $@
	
clean:
	-rm -rf build/
	-rm *.pyc
	-rm *.so
	-rm *.c
	-rm *_ui.py
	