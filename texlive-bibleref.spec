Name:		texlive-bibleref
Version:	55626
Release:	1
Summary:	Format bible citations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bibleref
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref.r55626.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref.doc.r55626.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bibleref.source.r55626.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bibleref package offers consistent formatting of references
to parts of the Christian bible, in a number of well-defined
formats.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bibleref
%doc %{_texmfdistdir}/doc/latex/bibleref
#- source
%doc %{_texmfdistdir}/source/latex/bibleref

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
