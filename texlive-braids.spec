# revision 23790
# category Package
# catalog-ctan /graphics/pgf/contrib/braids
# catalog-date 2011-08-30 13:04:52 +0200
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-braids
Version:	1.0
Release:	2
Summary:	Draw braid diagrams with PGF/TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/braids
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/braids.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/braids.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/braids.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package enables drawing of braid diagrams with PGF/TikZ
using a simple syntax. The braid itself is specified by giving
a word in the braid group, and there are many options for
styling the strands and for drawing "floors".

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/braids/braids.sty
%doc %{_texmfdistdir}/doc/latex/braids/README
%doc %{_texmfdistdir}/doc/latex/braids/braids_doc.pdf
%doc %{_texmfdistdir}/doc/latex/braids/braids_doc.tex
#- source
%doc %{_texmfdistdir}/source/latex/braids/braids.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
