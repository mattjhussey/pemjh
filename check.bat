@setlocal
@for /R %%f in (*.pyc) do @del %%f
flake8 pemjh --show-source --show-pep8
pylint pemjh
@set pytest=py.test pemjh --showlocals --full-trace --durations=0 --doctest-modules
@set pytestargs=
@if "%1"=="NOCOV" (
	@call set pytestargs=%%pytestargs%% -p no:cov
) else (
	@call set pytestargs=%%pytestargs%% --cov=pemjh --cov-report=term-missing --cov-report=html
	@if "%1"=="TOLCOV" (
		@call set pytestargs=%%pytestargs%%
	) else (
		@call set pytestargs=%%pytestargs%% --cov-fail-under=100
	)
)
%pytest% %pytestargs%
@endlocal