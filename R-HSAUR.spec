%global packname  HSAUR
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.3_0
Release:          1
Summary:          A Handbook of Statistical Analyses Using R
Group:            Sciences/Mathematics
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.3-0.tar.gz
Requires:         R-lattice R-MASS R-scatterplot3d R-ape R-coin R-flexmix
Requires:         R-gee R-ipred R-lme4 R-mclust R-party R-randomForest
Requires:         R-rmeta R-vcd R-survival R-KernSmooth R-rpart R-mvtnorm
Requires:         R-Matrix R-boot
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-lattice R-MASS R-scatterplot3d R-ape R-coin R-flexmix
BuildRequires:    R-gee R-ipred R-lme4 R-mclust R-party R-randomForest
BuildRequires:    R-rmeta R-vcd R-survival R-KernSmooth R-rpart R-mvtnorm
BuildRequires:    R-Matrix R-boot 

%description
Functions, data sets, analyses and examples from the book `A Handbook of
Statistical Analyses Using R' (Brian S. Everitt and Torsten Hothorn,
Chapman & Hall/CRC, 2006). The first chapter of the book, which is
entitled `An Introduction to R', is completely included in this package,
for all other chapters, a vignette containing all data analyses is

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CHANGES
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/cache
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/rawdata
