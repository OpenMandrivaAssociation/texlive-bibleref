%global tl_name bibleref
%global tl_revision 75257

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.26.0
Release:	%{tl_revision}.1
Summary:	Format bible citations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bibleref
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bibleref package offers consistent formatting of references to parts
of the Christian bible, in a number of well-defined formats. It depends
on ifthen, fmtcount, and amsgen.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bibleref
%dir %{_datadir}/texmf-dist/source/latex/bibleref
%dir %{_datadir}/texmf-dist/tex/latex/bibleref
%dir %{_datadir}/texmf-dist/doc/latex/bibleref/samples
%doc %{_datadir}/texmf-dist/doc/latex/bibleref/CHANGELOG-bibleref.md
%doc %{_datadir}/texmf-dist/doc/latex/bibleref/README.md
%doc %{_datadir}/texmf-dist/doc/latex/bibleref/bibleref.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bibleref/makefile
%doc %{_datadir}/texmf-dist/doc/latex/bibleref/sample.ist
%doc %{_datadir}/texmf-dist/doc/latex/bibleref/samples/sample-categories.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bibleref/samples/sample-indextools.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bibleref/samples/sample-xidx.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bibleref/samples/sample.pdf
%doc %{_datadir}/texmf-dist/source/latex/bibleref/bibleref.dtx
%doc %{_datadir}/texmf-dist/source/latex/bibleref/bibleref.ins
%{_datadir}/texmf-dist/tex/latex/bibleref/bibleref-xidx.sty
%{_datadir}/texmf-dist/tex/latex/bibleref/bibleref.sty
