all:
run:
	@python run.py 
clean:
	@find . -type f -name "*.pyc" -exec rm -f {} \;
	@find . -type d -name "__pycache__" -delete
	@find . -type d -name ".pytest_cache" -exec rm -rvf {} \;
	@find . -type d -name ".vscode" -exec rm -rvf {} \;

update:
	@git add -A
	@git commit -a -m "update"
	@git push
