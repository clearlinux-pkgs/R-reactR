#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-reactR
Version  : 0.4.4
Release  : 43
URL      : https://cran.r-project.org/src/contrib/reactR_0.4.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/reactR_0.4.4.tar.gz
Summary  : React Helpers
Group    : Development/Tools
License  : MIT
Requires: R-htmltools
BuildRequires : R-htmltools
BuildRequires : buildreq-R

%description
helper dependency functions, an embedded 'Babel' 'transpiler',
              and examples.

%prep
%setup -q -c -n reactR
cd %{_builddir}/reactR

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641091409

%install
export SOURCE_DATE_EPOCH=1641091409
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library reactR
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library reactR
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library reactR
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc reactR || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/reactR/DESCRIPTION
/usr/lib64/R/library/reactR/INDEX
/usr/lib64/R/library/reactR/LICENSE
/usr/lib64/R/library/reactR/Meta/Rd.rds
/usr/lib64/R/library/reactR/Meta/features.rds
/usr/lib64/R/library/reactR/Meta/hsearch.rds
/usr/lib64/R/library/reactR/Meta/links.rds
/usr/lib64/R/library/reactR/Meta/nsInfo.rds
/usr/lib64/R/library/reactR/Meta/package.rds
/usr/lib64/R/library/reactR/Meta/vignette.rds
/usr/lib64/R/library/reactR/NAMESPACE
/usr/lib64/R/library/reactR/NEWS.md
/usr/lib64/R/library/reactR/R/reactR
/usr/lib64/R/library/reactR/R/reactR.rdb
/usr/lib64/R/library/reactR/R/reactR.rdx
/usr/lib64/R/library/reactR/doc/index.html
/usr/lib64/R/library/reactR/doc/intro_htmlwidgets.R
/usr/lib64/R/library/reactR/doc/intro_htmlwidgets.Rmd
/usr/lib64/R/library/reactR/doc/intro_htmlwidgets.html
/usr/lib64/R/library/reactR/doc/intro_inputs.R
/usr/lib64/R/library/reactR/doc/intro_inputs.Rmd
/usr/lib64/R/library/reactR/doc/intro_inputs.html
/usr/lib64/R/library/reactR/doc/intro_reactR.R
/usr/lib64/R/library/reactR/doc/intro_reactR.Rmd
/usr/lib64/R/library/reactR/doc/intro_reactR.html
/usr/lib64/R/library/reactR/examples/antd.R
/usr/lib64/R/library/reactR/examples/office-fabric.R
/usr/lib64/R/library/reactR/help/AnIndex
/usr/lib64/R/library/reactR/help/aliases.rds
/usr/lib64/R/library/reactR/help/paths.rds
/usr/lib64/R/library/reactR/help/reactR.rdb
/usr/lib64/R/library/reactR/help/reactR.rdx
/usr/lib64/R/library/reactR/html/00Index.html
/usr/lib64/R/library/reactR/html/R.css
/usr/lib64/R/library/reactR/templates/input_app.R.txt
/usr/lib64/R/library/reactR/templates/input_js.txt
/usr/lib64/R/library/reactR/templates/input_r.txt
/usr/lib64/R/library/reactR/templates/package.json.txt
/usr/lib64/R/library/reactR/templates/webpack.config.js.txt
/usr/lib64/R/library/reactR/templates/widget_app.R.txt
/usr/lib64/R/library/reactR/templates/widget_js.txt
/usr/lib64/R/library/reactR/templates/widget_r.txt
/usr/lib64/R/library/reactR/templates/widget_yaml.txt
/usr/lib64/R/library/reactR/www/babel/babel.min.js
/usr/lib64/R/library/reactR/www/core-js/LICENSE
/usr/lib64/R/library/reactR/www/core-js/package.json
/usr/lib64/R/library/reactR/www/core-js/shim.min.js
/usr/lib64/R/library/reactR/www/mobx/LICENSE
/usr/lib64/R/library/reactR/www/mobx/mobx-react-lite.js
/usr/lib64/R/library/reactR/www/mobx/mobx-react.umd.js
/usr/lib64/R/library/reactR/www/mobx/mobx.min.js
/usr/lib64/R/library/reactR/www/mobx/mobx.umd.min.js
/usr/lib64/R/library/reactR/www/mobx/package.json
/usr/lib64/R/library/reactR/www/react-tools/react-tools.js
/usr/lib64/R/library/reactR/www/react-tools/react-tools.js.map
/usr/lib64/R/library/reactR/www/react/AUTHORS
/usr/lib64/R/library/reactR/www/react/LICENSE.txt
/usr/lib64/R/library/reactR/www/react/react-dom.min.js
/usr/lib64/R/library/reactR/www/react/react.min.js
