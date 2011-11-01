Name:		texlive-bibleref
Version:	1.14
Release:	1
Summary:	Format bible citations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bibleref
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The bibleref package offers consistent formatting of references
to parts of the Christian bible, in a number of well-defined
formats.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bibleref/bibleref.sty
%doc %{_texmfdistdir}/doc/latex/bibleref/CHANGES
%doc %{_texmfdistdir}/doc/latex/bibleref/README
%doc %{_texmfdistdir}/doc/latex/bibleref/bibleref-manual.css
%doc %{_texmfdistdir}/doc/latex/bibleref/bibleref-manual.html
%doc %{_texmfdistdir}/doc/latex/bibleref/bibleref-manual.tex
%doc %{_texmfdistdir}/doc/latex/bibleref/bibleref.pdf
%doc %{_texmfdistdir}/doc/latex/bibleref/samples/sample-categories.pdf
%doc %{_texmfdistdir}/doc/latex/bibleref/samples/sample-categories.tex
%doc %{_texmfdistdir}/doc/latex/bibleref/samples/sample-multind.pdf
%doc %{_texmfdistdir}/doc/latex/bibleref/samples/sample-multind.tex
%doc %{_texmfdistdir}/doc/latex/bibleref/samples/sample-xidx.pdf
%doc %{_texmfdistdir}/doc/latex/bibleref/samples/sample-xidx.tex
%doc %{_texmfdistdir}/doc/latex/bibleref/samples/sample.ist
%doc %{_texmfdistdir}/doc/latex/bibleref/samples/sample.pdf
%doc %{_texmfdistdir}/doc/latex/bibleref/samples/sample.tex
#- source
%doc %{_texmfdistdir}/source/latex/bibleref/bibleref.dtx
%doc %{_texmfdistdir}/source/latex/bibleref/bibleref.ins
%doc %{_texmfdistdir}/source/latex/bibleref/bibleref.perl

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
