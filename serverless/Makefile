.PHONY: deploy
deploy:
	sls deploy

.PHONY: todo
todo:
	rg -A3 '(TODO|FIXME)' .

.PHONY: black
black: # Lint the codebase with black.
	black app

.PHONY: test
test:
	pytest

.PHONY: test-sls
test-sls:
	sls invoke local --function get_url --path test/templates/get_url.json
	sls invoke local --function get_url_by_pathparam --path test/templates/get_url_by_pathparam.json
	sls invoke local --function set_url --path test/templates/set_url.json
	sls invoke local --function redirect_url --path test/templates/redirect_url.json