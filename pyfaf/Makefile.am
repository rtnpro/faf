SUBDIRS = client emergency hub worker storage

pyfaf_PYTHON = \
	__init__.py \
	argparse.py \
	bugzilla.py \
	cluster.py \
	common.py \
	queries.py \
	kb.py \
	libsolv.py \
	obs.py \
	package.py \
	retrace.py \
	support.py \
	ureport.py \
	terminal.py \
	template.py
pyfafdir = $(pythondir)/pyfaf

nodist_config_SCRIPTS = config.py
configdir = $(pyfafdir)

edit = sed \
	-e 's|@version[@]|$(PACKAGE_VERSION)|g' \
	-e 's|@bindir[@]|$(bindir)|g' \
	-e 's|@sysconfdir[@]|$(sysconfdir)|g' \
	-e 's|@prefix[@]|$(prefix)|g' \
	-e 's|@datadir[@]|$(datadir)|g' \
	-e 's|@libdir[@]|$(libdir)|g'

EXTRA_DIST = config.py.in
config.py: config.py.in Makefile
	$(edit) $< > $@
