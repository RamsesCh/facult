'use strict';
var app = angular.module('App2', ['ngStorage',
                                  'ngRoute',
                                  'ngPagination',
                                  'ngFileUpload',
                                  'ngDialog',
                                  'angucomplete-alt']);
var app3 = angular.module('App3', ['ngStorage']);

    app.config(function ($routeProvider) {
        $routeProvider.when('/', {
            controller: 'MainCtrl',
            templateUrl: '/templates/home.html',
            resolve: {
                'guestService': 'facultService'
            },
        });
        $routeProvider.when('/invite', {
            controller: 'InsertCtrl',
            templateUrl: '/templates/new.html',
            resolve: {
                'guestService': 'ramoService',
                'guestService2': 'tipo_pagoService',
                'guestService3': 'linea_negoService',
                'guestService5': 'conceptoService',
                'guestService6': 'motivoService',
                'guestService7': 'detalleService',
                'guestService8': 'tipoFondoService',
                'guestService10': 'faeService',
                'guestService11': 'userService'
            }
        });
        $routeProvider.when('/view/:id_facultamiento', {
            controller: 'detCtrl',
            templateUrl: '/templates/detalle.html',
            resolve: {
                'guestService': 'facultService'
            },
        });
        $routeProvider.when('/edocta', {
            controller: 'edoctaCtrl',
            templateUrl: '/templates/edo_cta.html',
            resolve: {
                'guestService2': 'userService'
            }
        });
        $routeProvider.when('/estadist', {
            controller: 'estadistCtrl',
            templateUrl: '/templates/estadist.html',
            resolve: {
                'guestService': 'reportsService'
            }
        });
        $routeProvider.when('/admin_cat', {
            controller: 'adminCatCtrl',
            templateUrl: '/templates/admin_cat.html',
            resolve: {
                'guestService': 'tipo_pagoService',
                'guestService2': 'conceptoService',
                'guestService3': 'detalleService'
            }
        });
        $routeProvider.when('/admin_usr', {
            controller: 'adminUsersCtrl',
            templateUrl: '/templates/admin_usr.html',
            resolve: {
                'guestService': 'userService',
                'guestService2': 'perfilService',
                'guestService3': 'direccionesService',
                'guestService4': 'puestosService',
                'guestService5': 'aspectosService'
            }
        });
        $routeProvider.when('/editUser/:id_usuario', {
            controller: 'editUserCtrl',
            templateUrl: '/templates/edit_user.html',
            resolve: {
                'guestService2': 'perfilService',
                'guestService3': 'direccionesService',
                'guestService4': 'puestosService',
                'guestService5': 'aspectosService' 
            }
        });
        $routeProvider.when('/admin_fond', {
            controller: 'adminFondCtrl',
            templateUrl: '/templates/admin_fond.html',
            resolve: {
                'guestService': 'fondoService',
                'guestService2': 'userService',
                'guestService3': 'ramoService',
                'guestService4': 'linea_negoService',
            }
        });
        $routeProvider.when('/update_fondo/:id_fondo', {
            controller: 'editFondoCtrl',
            templateUrl: '/templates/edit_fondo.html',
        });
        $routeProvider.when('/politicas', {
            controller: 'politCtrl',
            templateUrl: '/templates/politicas.html',
            resolve: {
                'guestService': 'politicasService'
            }
        });
        $routeProvider.when('/ayuda', {
            templateUrl: '/templates/ayuda.html',
        });
        $routeProvider.otherwise({
            redirectTo: '/'
        });
    });
    /* factory de catalogos*/
    app.factory('facultService', function ($rootScope, $http, $q, $log, $parse) {
        var deferred = $q.defer();
        $http.get('rest/query')
            .success(function (data, status, headers, config) {
                $rootScope.facults = data;
                deferred.resolve();
            });
        return deferred.promise;
    });
    app.factory('faeService', function ($rootScope, $http, $q, $log) {
        var deferred = $q.defer();
        $http.get('rest/cat_tipo_fae')
            .success(function (data, status, headers, config) {
                $rootScope.fae = data;
                deferred.resolve();
                //console.log(data);
            });
        return deferred.promise;
    });
    app.factory('ramoService', function ($rootScope, $http, $q, $log) {
        var deferred = $q.defer();
        $http.get('rest/cat')
            .success(function (data, status, headers, config) {
                $rootScope.ramo = data;
                deferred.resolve();
                //console.log(data);
            });
        return deferred.promise;
    });
    app.factory('tipo_pagoService', function ($rootScope, $http, $q, $log) {
        var deferred = $q.defer();
        $http.get('rest/cat_tipo_pago')
            .success(function (data2, status, headers, config) {
                $rootScope.tipo_pago = data2;
                deferred.resolve();
                //console.log(data2);
            });
        return deferred.promise;
    });
    app.factory('linea_negoService', function ($rootScope, $http, $q, $log) {
        var deferred = $q.defer();
        $http.get('rest/cat_linea_nego')
            .success(function (data, status, headers, config) {
                $rootScope.cat_linea_nego = data;
                deferred.resolve();
                //console.log(data2);
            });
        return deferred.promise;
    });
    app.factory('conceptoService', function ($rootScope, $http, $q, $log) {
        var deferred = $q.defer();
        $http.get('rest/cat_concepto')
            .success(function (data, status, headers, config) {
                $rootScope.cat_concepto = data;
                deferred.resolve();
                //console.log(data2);
            });
        return deferred.promise;
    });
    app.factory('motivoService', function ($rootScope, $http, $q, $log) {
        var deferred = $q.defer();
        $http.get('rest/cat_motivo')
            .success(function (data, status, headers, config) {
                $rootScope.cat_motivo = data;
                deferred.resolve();
                //console.log(data2);
            });
        return deferred.promise;
    });
    app.factory('detalleService', function ($rootScope, $http, $q, $log) {
        var deferred = $q.defer();
        $http.get('rest/cat_detalle')
            .success(function (data, status, headers, config) {
                $rootScope.cat_detalle = data;
                deferred.resolve();
                //console.log(data2);
            });
        return deferred.promise;
    });
    app.factory('tipoFondoService', function ($rootScope, $http, $q, $log) {
        var deferred = $q.defer();
        $http.get('rest/cat_tipoFondo')
            .success(function (data, status, headers, config) {
                $rootScope.cat_tipoFondo = data;
                deferred.resolve();
                //console.log(data2);
            });
        return deferred.promise;
    });
    app.factory('userService', function ($rootScope, $http, $q, $log) {
        var deferred = $q.defer();
        $http.get('rest/admin_users')
            .success(function (data, status, headers, config) {
                $rootScope.cat_users = data;
                deferred.resolve();
                //console.log(data);
            });
        return deferred.promise;
    });
    app.factory('perfilService', function ($rootScope, $http, $q, $log) {
        var deferred = $q.defer();
        $http.get('rest/cat_perfiles')
            .success(function (data, status, headers, config) {
                $rootScope.cat_perfiles = data;
                deferred.resolve();
                //console.log(data2);
            });
        return deferred.promise;
    });
    app.factory('fondoService', function ($rootScope, $http, $q, $log) {
        var deferred = $q.defer();
        $http.get('rest/admin_fondos')
            .success(function (data, status, headers, config) {
                $rootScope.cat_fondos = data;
                deferred.resolve();
                //console.log(data2);
            });
        return deferred.promise;
    });
    app.factory('direccionesService', function ($rootScope, $http, $q, $log) {
        var deferred = $q.defer();
        $http.get('rest/cat_direcciones')
            .success(function (data, status, headers, config) {
                $rootScope.cat_direcc = data;
                deferred.resolve();
                //console.log(data2);
            });
        return deferred.promise;
    });
    app.factory('puestosService', function ($rootScope, $http, $q, $log) {
        var deferred = $q.defer();
        $http.get('rest/cat_puestos')
            .success(function (data, status, headers, config) {
                $rootScope.cat_puestos = data;
                deferred.resolve();
                //console.log(data2);
            });
        return deferred.promise;
    });
    app.factory('aspectosService', function ($rootScope, $http, $q, $log) {
        var deferred = $q.defer();
        $http.get('rest/cat_aspectos')
            .success(function (data, status, headers, config) {
                $rootScope.cat_aspectos = data;
                deferred.resolve();
                //console.log(data2);
            });
        return deferred.promise;
    });
    app.factory('reportsService', function ($rootScope, $http, $q, $log) {
        var deferred = $q.defer();
        $http.get('rest/reports')
            .success(function (data, status, headers, config) {
                $rootScope.reports = data;
                deferred.resolve();
                //console.log(data2);
            });
        return deferred.promise;
    });
    app.factory('politicasService', function ($rootScope, $http, $q, $log) {
        var deferred = $q.defer();
        $http.get('rest/politicas')
            .success(function (data, status, headers, config) {
                $rootScope.politicas = data;
                deferred.resolve();
                //console.log(data2);
            });
        return deferred.promise;
    });
    /* factory de catalogos*/
    /* controllers*/
    app3.controller('gac', function ($scope, $window, $q, $http, $rootScope, $location, $sessionStorage, $timeout) {
        $scope.solicAccesAlert = false;
        var auth2;
        $scope.user = {};
        
        $window.appStart = function () {
            gapi.load('auth2', initSigninV2);
        };
        var initSigninV2 = function () {
            auth2 = gapi.auth2.getAuthInstance();
            auth2.isSignedIn.listen(signinChanged);
            auth2.currentUser.listen(userChanged);

            if (auth2.isSignedIn.get() == true) {
                auth2.signIn();
            }
        };

        var signinChanged = function (isSignedIn) {
            if (isSignedIn) {
                var googleUser = auth2.currentUser.get();
                var authResponse = googleUser.getAuthResponse();
                var profile = googleUser.getBasicProfile();
                $scope.user.id = profile.getId();
                $scope.user.fullName = profile.getName();
                $scope.user.firstName = profile.getGivenName();
                $scope.user.lastName = profile.getFamilyName();
                $scope.user.photo = profile.getImageUrl();
                $scope.user.email = profile.getEmail();
                $scope.user.domain = googleUser.getHostedDomain();
                $scope.user.timestamp = moment().format('x');
                $scope.user.idToken = authResponse.id_token;
                $scope.user.expiresAt = authResponse.expires_at;
                $scope.$digest();
            } 
            else {
                $scope.user = {};
                $scope.$digest();
            }
            $rootScope.user = $scope.user;
        };
        var userChanged = function (user) {
        };
        
//botton continuar//
        $scope.submitLogin = function () {
            var deferred = $q.defer();
            $http.get('rest/admin_users')
                .success(function (data, status, headers, config) {
                    var salida = [];
                    angular.forEach(data, function(value, key){
                        if (value.email == $scope.user.email && value.activo ==1)
                            salida.push(value);
                    })
                    deferred.resolve();
                    if (salida.length > 0){
                        $scope.userData = {
                            'id_user':salida[0].id_usuario,
                            'name': $scope.user.firstName,
                            'email':$scope.user.email,
                            'perfil':salida[0].perfil,
                            'img':$scope.user.photo
                        };
                        $sessionStorage.userLocal = $scope.userData;
                        loginSuccess();
                        $window.location.href=('index.html')
                    }
                    else {
                        loginError();
                        $scope.solicAccesAlert = true;
                    }
                });
            return deferred.promise;
        }
//botton continuar//
    });
    app.controller('MasterController', function ($scope, $location, $rootScope, $window, $sessionStorage, ngDialog) {
        $scope.userActivo = $sessionStorage.userLocal;
        //console.log($scope.userActivo);
        if ($scope.userActivo == undefined){
            console.log("no se ha definido el usuario")
            $window.location.href=('/')
        }
        //MARCAR LOS MENUS COMO ACTIVOS//
        $scope.isActive = function (destination) {
            return destination === $location.path();
        }
        //MARCAR LOS MENUS COMO ACTIVOS//
        $scope.clickToOpen2 = function (report) {
            //console.log(report)
            ngDialog.open({
                template: 'templates/ayuda.html',
                plain: false,
                closeByDocument: false,
                className: 'ngdialog-theme-default',
                width: '50%',
                height: '1000'
            });
        };
    });
    app.controller('MainCtrl', function ($scope, $rootScope, $log, $http, $routeParams, $location, $route, $q, $window, $timeout) {
        $rootScope.overlayLoad = false;
        var facults = $rootScope.facults;
        var faesAut = [];
        angular.forEach(facults, function(value, key){
            if (value.id_estatus == 4)
                faesAut.push(value);
        })
        console.log(faesAut.length)
        
        $scope.sortType     = '-id_facultamiento'; // set the default sort type
        $scope.sortReverse  = false;
        
        var salida = [];
        if($scope.userActivo.perfil == 'ADMIN' || $scope.userActivo.perfil == 'GOD' || $scope.userActivo.perfil == 'CONSULTA'){
            $scope.facultList = facults;
        }
        else if ($scope.userActivo.perfil == 'FUNCIONARIO'){
            angular.forEach(facults, function(value, key){
            if (value.id_solicitante == $scope.userActivo.id_user || value.id_func_vb == $scope.userActivo.id_user)
                salida.push(value);
            })
        $scope.facultList = salida;
        }
        else if ($scope.userActivo.perfil == 'SOLICITANTE'){
            angular.forEach(facults, function(value, key){
            if (value.id_solicitante == $scope.userActivo.id_user)
                salida.push(value);
            })
        $scope.facultList = salida;
        }
           
        
    });
    app.controller('InsertCtrl', function ($scope, $rootScope, $log, $http, $routeParams, $location, $route, Upload, $timeout, $window, $q) {
        //var locAbs = $location.absUrl();
        //console.log(locAbs);
        //console.log($scope.userActivo.name);
        //console.log($scope.userActivo.id_user);
        //CATÁLOGOS ALMACENADOS EN $SCOOPE//
        $scope.cat_tipos_fae = $rootScope.fae;
        $scope.cat_ramo = $rootScope.ramo;
        $scope.cat_linea_nego = $rootScope.cat_linea_nego;
        $scope.cat_tipo_pago = $rootScope.tipo_pago;
        $scope.cat_afectacion = $rootScope.cat_afectacion;
        $scope.cat_concepto = $rootScope.cat_concepto;
        $scope.cat_detalle = $rootScope.cat_detalle;
        //$scope.cat_func = $rootScope.cat_func;
        $scope.cat_users = $rootScope.cat_users
        //console.log($scope.cat_tipo_pago)
        $scope.picFiles = "";
        //CATÁLOGOS ALMACENADOS EN $SCOOPE//
        
        $scope.activOverload = function(){
            $rootScope.overlayLoad = true;
            /*
            $timeout(function() {
                $rootScope.overlayLoad = false;
                $location.path('/');
                $window.location.reload()
                altaAlert();
            },20000);*/
        }
        
        
        //QUITAR LINEA NEGO N/A//
        var lineanegoSalida = [];
        angular.forEach($scope.cat_linea_nego, function(value, key){
            if (value.linea_nego != 'N/A'){
                lineanegoSalida.push(value)
            }
        })
        $scope.catLineaNego = lineanegoSalida;
        //QUITAR LINEA NEGO N/A//
        
        
        //FILTRAR USUARIOS, DEJAR SOLO FUNCIONARIOS//
        var usersSalida = [];
        angular.forEach($scope.cat_users, function (value, key) {
            if (value.perfil == 'FUNCIONARIO' && value.activo == 1) {
                    usersSalida.push(value);
            }
        })
        $scope.usersFunc = usersSalida;
        //FILTRAR USUARIOS, DEJAR SOLO FUNCIONARIOS//
        
       //desactivar campos si es ADMINTIVO// 
        $scope.tipoFAE = function (id_tipo_fae) {
            if ($scope.id_tipo_fae === "2") {
                $scope.id_tipo_fondo = "3";
                $scope.id_funcionario = 1;
                $scope.fondo_actual = 1;
                $scope.fondo_restante = 1;
                $scope.id_motivo = 7;
                $scope.id_detalle = 29;
                $scope.folio_nvo_barra = "N/A";
                $scope.required = false;
                $scope.cat_tipo_fondo = $rootScope.cat_tipoFondo;
                console.log($scope.required)
            } else {
                $scope.id_tipo_fondo = "";
                $scope.id_motivo = "";
                $scope.id_detalle = "";
                
                $scope.required = true;
                var tipFonOut = [];
                angular.forEach($rootScope.cat_tipoFondo, function (value, key) {
                    if (value.tipo_fondo != 'N/A') {
                        tipFonOut.push(value);
                    }
                })
                $scope.cat_tipo_fondo = tipFonOut;
                //console.log($scope.required)
            }
        }
        //desactivar campos si es ADMINTIVO//
        
        //SI RAMO == AUTOS, NO SE REQUIERE FOLIO BARRA//
        $scope.desFolioBarra = function (id_ramo) {
            if (id_ramo === "2") {
                $scope.folio_nvo_barra = "N/A";
            } else if (id_ramo === "3") {
                $scope.folio_nvo_barra = "N/A";
            } else if (id_ramo == "1"){
                $scope.folio_nvo_barra = "";
            }
        }
        //SI RAMO == AUTOS, NO SE REQUIERE FOLIO BARRA//
        
        //SI TIPO DE FONDO == FUNC, ID_FUNC_VB = ID_FUNC//
        $scope.desTipoFondo = function (id_tipo_fondo) {
            if (id_tipo_fondo === "1") {
                $scope.id_funcionario = 1;
                //console.log($scope.id_funcionario)
            }
            
            else if (id_tipo_fondo === "2"){
                $scope.id_funcionario = " ";
                $scope.id_func_vb = " ";
                //console.log($scope.id_funcionario)
                //console.log($scope.id_func_vb)
            }
            else if (id_tipo_fondo === "3") {
                $scope.id_funcionario = 1;
                //console.log($scope.id_funcionario)
            }
        }
        //SI TIPO DE FONDO == FUNC, ID_FUNC_VB = ID_FUNC//
        
        // CONSULTA GASTOS Y FONDOS DISPONIBLES DE FUNC//
        $scope.customSelected = function(selected){
            if (selected) {
                var id_funcionario = selected.originalObject.id_usuario;
                $scope.func_vb = selected.originalObject.nombre + " " + selected.originalObject.ap_pat + " " + selected.originalObject.ap_mat;
                var id_ramo = $scope.id_ramo;
                var id_linea_nego = $scope.id_linea_nego;
                
                $scope.id_funcionario = id_funcionario;
                $scope.id_func_vb = id_funcionario;
                //console.log($scope.id_func_vb)
                
                if (id_funcionario === 350) {
                    //console.log("es el jefaso");
                    $scope.fondo_actual = 1;
                    $scope.fondo_restante = 1;
                } else {
                    $http.get('rest/consult_monto')
                        .success(function (data, headers, config) {
                            var montos = data;
                            if (id_ramo === "1") {
                                var salida = [];
                                angular.forEach(montos, function (value, key) {
                                    if (value.id_ramo == id_ramo && value.id_linea_nego == id_linea_nego && value.id_funcionario == id_funcionario) {
                                        salida.push(value);
                                    }
                                })
                                $http.get('rest/consult_gastos')
                                    .success(function (data, headers, config) {
                                        var gastos = data;
                                        var salida2 = [];
                                        angular.forEach(gastos, function (value, key) {
                                            if (value.id_ramo == id_ramo && value.id_linea_nego == id_linea_nego && value.id_funcionario == id_funcionario) {
                                                salida2.push(value);
                                            }
                                        })
                                        montos = salida;
                                        if (montos.length <= 0) {
                                            console.log("no hay fondo")
                                            $scope.monto = 0;
                                        } else {
                                            $scope.monto = montos[0].monto;
                                        }
                                        console.log($scope.monto);

                                        gastos = salida2;
                                        if (gastos.length <= 0) {
                                            //console.log("aun no hay gastos")
                                            $scope.gasto = 0;
                                        } else {
                                            $scope.gasto = gastos[0].total_aut;
                                        }
                                        console.log($scope.gasto);
                                        $scope.fondo_actual = $scope.monto - $scope.gasto;
                                        //console.log($scope.fondo_actual);
                                    })

                            } 
                            else if (id_ramo === "2") {
                                var salida = [];
                                angular.forEach(montos, function (value, key) {
                                    if (value.id_ramo == id_ramo && value.id_funcionario == id_funcionario) {
                                        //console.log(value);
                                        salida.push(value);
                                    }
                                })
                                $http.get('rest/consult_gastos_autos')
                                    .success(function (data, headers, config) {
                                        var gastos = data;
                                        //console.log(gastos)
                                        var salida2 = [];
                                        angular.forEach(gastos, function (value, key) {
                                            if (value.id_ramo == id_ramo && value.id_funcionario == id_funcionario) {
                                                salida2.push(value);
                                            }
                                        })
                                        montos = salida;
                                        //console.log(montos)
                                        if (montos.length <= 0) {
                                            console.log("no hay fondos")
                                            $scope.monto = 0;
                                        } else {
                                            $scope.monto = montos[0].monto;
                                        }
                                        //console.log($scope.monto);

                                        gastos = salida2;
                                        //console.log(gastos)
                                        if (gastos.length <= 0) {
                                            console.log("no hay gasto")
                                            $scope.gasto = 0;
                                        } else {
                                            $scope.gasto = gastos[0].total_aut;
                                        }
                                        //console.log($scope.gasto);
                                        $scope.fondo_actual = $scope.monto - $scope.gasto;
                                        //console.log($scope.fondo_actual);
                                })
                            }
                        })
                }
                
                var motivosSalida = [];
                angular.forEach($rootScope.cat_motivo, function (value, key) {
                    if (value.id_func == selected.originalObject.id_usuario) {
                            motivosSalida.push(value);
                    }
                })
                $scope.catMotivos = motivosSalida;                 
            } else {
                console.log('');
            }
            
        }
        // CONSULTA GASTOS Y FONDOS DISPONIBLES DE FUNC//
        
        // obtener id func vb//
        $scope.customSelected2 = function(selected){
            $scope.id_func_vb = selected.originalObject.id_usuario;
            var motivosSalida = [];
                angular.forEach($rootScope.cat_motivo, function (value, key) {
                    if (value.id_func == selected.originalObject.id_usuario) {
                            motivosSalida.push(value);
                    }
                })
                $scope.catMotivos = motivosSalida;
        }
        // obtener id func vb//
        
        //OBTIENE EL FONDO RESTANTE//
        $scope.compMonto = function (id_tipo_fae) {
            if (id_tipo_fae === "2" || $scope.id_funcionario == "350") {
                $scope.fondo_restante = "1"
                //console.log("mario vela o es admin")
            }
            else {
                //console.log("es otro")
                $scope.fondo_restante = $scope.fondo_actual - $scope.monto_autorizado;
            }
        }
        //OBTIENE EL FONDO RESTANTE//
        
        //SELECCIONAR ARCHIVOS Y ALMACENARLOS EN ARREGLO //
        $scope.uploadFiles = function(files, errFiles) {
            $scope.picFiles = files;
            $scope.errFiles = errFiles;
            console.log()
        }
        //SELECCIONAR ARCHIVOS Y ALMACENARLOS EN ARREGLO //
        
        //INSERTA LOS DATOS EN LA BASE//
        $scope.submitInsert = function () {
            if ($scope.folio_nvo_barra == "") {
                $scope.folio_nvo_barra = "N/A";
            }
            if ($scope.reclamacion == null) {
                $scope.reclamacion = "N/A";
            }
            if ($scope.nombre_benef == null) {
                $scope.nombre_benef = "N/A"
            }
            if ($scope.ap_pat_benef == null) {
                $scope.ap_pat_benef = "N/A"
            }
            if ($scope.ap_mat_benef == null) {
                $scope.ap_mat_benef = "N/A"
            }
            if ($scope.causa == null) {
                $scope.causa = "N/A"
            }
            var facult = {
                id_tipo_fae: $scope.id_tipo_fae,
                id_solicitante: $scope.userActivo.id_user,
                email_solicitante: $scope.userActivo.email,
                siniestro: $scope.siniestro,
                poliza: $scope.poliza,
                reclamacion: $scope.reclamacion,
                id_linea_nego: $scope.id_linea_nego,
                id_ramo: $scope.id_ramo,
                nombre_benef: $scope.nombre_benef,
                ap_pat_benef: $scope.ap_pat_benef,
                ap_mat_benef: $scope.ap_mat_benef,
                folio_nvo_barra: $scope.folio_nvo_barra,
                id_tipo_pago: $scope.id_tipo_pago,
                id_concepto: $scope.id_concepto,
                id_motivo: $scope.id_motivo,
                id_detalle: $scope.id_detalle,
                causa: $scope.causa,
                id_tipo_fondo: $scope.id_tipo_fondo,
                id_funcionario: $scope.id_funcionario,
                monto_autorizado: $scope.monto_autorizado,
                fondo_actual: $scope.fondo_actual,
                fondo_restante: $scope.fondo_restante,
                id_func_vb: $scope.id_func_vb,
                archivos: $scope.picFiles,
            };
            //console.log(facult)
            $http.post('/rest/insert', facult)
                .success(function (data, status, headers, config) {
                    $rootScope.facults.push(data);
                    //console.log(data);
                    var loopPromises = [];
                    angular.forEach($scope.picFiles, function(file) {
                        var deferred = $q.defer();
                        loopPromises.push(deferred.promise);
                        
                        var datFiles = {
                            id_facultamiento: data,
                            archivos: file
                        };
                        //console.log(datFiles);
                        file.upload = Upload.upload({
                            url: 'rest/upload_files',
                            data: {id_facultamiento : data, archivos: file}
                        });
                        deferred.resolve();
                        //console.log()
                    });
                    $q.all(loopPromises).then(function () {
                        console.log('foreach loop completed. Do something after it...');
                        altaAlert();
                        $timeout(function () {
                            $location.path('/');
                            $window.location.reload()
                        }, 2000);
                    });
                });
            /*
            $location.path('/');
            altaAlert();
            $timeout(function() {
                $window.location.reload()
            },1500);*/
        }
        //INSERTA LOS DATOS EN LA BASE//
    });
    app.controller('detCtrl', function ($routeParams, $rootScope, $scope, $log, $http, $location, ngDialog, $timeout, $window) {
        for (var i = 0; i < $rootScope.facults.length; i++) {
            if ($rootScope.facults[i].id_facultamiento == $routeParams.id_facultamiento) {
                $scope.facult = angular.copy($rootScope.facults[i]);
            }
        }
        console.log()
        $http.post('rest/files',{id_facultamiento: $routeParams.id_facultamiento})
        .success(function(data,status,headers,config){
                $scope.files = data;
                //console.log($scope.files)
                $scope.totalfiles = Object.keys($scope.files).length;
        })
       
        //boton autorizar//
        $scope.submitAprobar = function (id_estatus, func_observ) {
            if (func_observ == null) {
                func_observ = "n/a"
            }
            var facult = {
                id_facultamiento: $routeParams.id_facultamiento,
                id_estatus: id_estatus,
                func_observ: func_observ
            }
            console.log(facult);
            $http.post('/rest/aprobar', facult)
                .success(function (data, status, headers, config) {
                    $rootScope.facults.push(data);
                });
            if (facult.id_estatus == 2){
                $location.path('/');
                aprobadoAlert();
                $timeout(function() {
                    $window.location.reload()
                },1500);
            }
            else{
                $location.path('/');
                rechazarAlert();
                $timeout(function() {
                    $window.location.reload()
                },1500);
            }
            //window.location.reload();
        }
        //boton autorizar//
        //boton terminar//
        $scope.submitTerminar = function (id_estatus, facult_observ) {
            if (facult_observ == null) {
                facult_observ = "n/a"
            }
            var facultamiento = {
                id_facultamiento: $routeParams.id_facultamiento,
                fecha_registro: $scope.facult.fecha_registro,
                solicitante: $scope.facult.solicitante,
                email_solic:$scope.facult.email_solicitante,
                monto_autorizado: $scope.facult.monto_autorizado,
                ramo: $scope.facult.ramo,
                linea_nego: $scope.facult.linea_nego,
                nom_benef: $scope.facult.nom_benef,
                appat_benef: $scope.facult.appat_benef,
                apmat_benef: $scope.facult.apmat_benef,
                id_estatus: id_estatus,
                facult_observ: facult_observ,
            }
            console.log(facultamiento);
            $http.post('/rest/terminar', facultamiento)
                .success(function (data, status, headers, config) {
                    $rootScope.facults.push(data);
                });
            if (facultamiento.id_estatus == 4){
                $location.path('/');
                terminarAlert();
                $timeout(function() {
                    $window.location.reload()
                },1500);
            }
            else{
                $location.path('/');
                cancelarAlert();
                $timeout(function() {
                    $window.location.reload()
                },1500);
            }
            
        }
        //boton terminar//
        //CANCELAR FAE//
        $scope.cancelFae = function(id_facult ,observ_cancel_folio, email_solicitante, email_func_vb, folio_termino, ramo, linea_nego, monto, nom_benef, appat_benef, apmat_benef){
            if (observ_cancel_folio == null) {
                observ_cancel_folio = "n/a"
            }
            var folioCancel = {
                id_facult: id_facult,
                observ_cancel_folio: observ_cancel_folio,
                email_solic: email_solicitante,
                email_func_vb: email_func_vb,
                folio_termino: folio_termino,
                ramo: ramo,
                linea_nego: linea_nego,
                monto: monto,
                nom_benef: nom_benef,
                appat_benef: appat_benef,
                apmat_benef: apmat_benef
            }
            console.log(folioCancel)
            $http.post('/rest/cancelaFolio', folioCancel)
            .success(function (data, status, headers, config){
                console.log(data)
                cancelarFolioAlert();
                $location.path('/')
            })
        }
        //CANCELAR FAE//
    });
    app.controller('edoctaCtrl', function ($scope, $http, $rootScope, $parse) {
            
        $scope.banEdocta = 0;
        $scope.funcSelect = {};
        $rootScope.navbarVal = 'activa';
        
        if ($scope.userActivo.perfil == 'GOD' || $scope.userActivo.perfil == 'ADMIN'){
            var listSalida = [];
            angular.forEach($rootScope.cat_users, function(value,key){
                if (value.perfil == 'FUNCIONARIO'){
                    listSalida.push(value)
                }
            })
        $scope.catFuncEdocta = listSalida;
        }
        else if ($scope.userActivo.perfil == 'FUNCIONARIO'){
            var listSalida = [];
            angular.forEach($rootScope.cat_users, function(value,key){
                if (value.perfil == 'FUNCIONARIO' &&  $scope.userActivo.id_user == value.id_usuario){
                    listSalida.push(value)
                }
            })
        $scope.catFuncEdocta = listSalida;         
        }
        
        $scope.consultEdocta = function (funcSelect, mesSelect) {
            $http.get('rest/edocta')
                .success(function (data, status, headers, config) {
                    var edocta = data;
                    var salida = [];
                    var total = 0
                    angular.forEach(edocta, function (value, key) {
                        if (value.id_func == funcSelect && value.mes == mesSelect) {
                            salida.push(value);
                        }
                    })
                    $scope.edocta = salida;
                    //console.log($scope.edocta)
                    
                    $scope.getTotal = function () {
                        var total = 0;
                        for (var i = 0; i < $scope.edocta.length; i++) {
                            var subt = parseFloat($scope.edocta[i].gmmlp);
                            var total = total + subt;
                        }
                        return total;
                    }
                    $scope.getTotal2 = function () {
                        var total = 0;
                        for (var i = 0; i < $scope.edocta.length; i++) {
                            var subt = parseFloat($scope.edocta[i].gmmlc);
                            var total = total + subt;
                        }
                        return total;
                    }
                    $scope.getTotal3 = function () {
                        var total = 0;
                        for (var i = 0; i < $scope.edocta.length; i++) {
                            var subt = parseFloat($scope.edocta[i].autos);
                            var total = total + subt;
                        }
                        //console.log(total)
                        return total;
                    }
                });
            $http.get('rest/edoctaMontos')
                .success(function (data, status, headers, config) {
                    var edoctaMontos = data;
                    var salida = [];
                    angular.forEach(edoctaMontos, function (value, key) {
                        if (value.id_func == funcSelect && value.mes == mesSelect) {
                            salida.push(value);
                        }
                    })
                    $scope.edoctaMontos = salida;
                    //console.log($scope.edoctaMontos)
                })
            $scope.banEdocta = 1;
        }
        
        /*
        $scope.getTotal = function () {
            var total = 0;
            for (var i = 0; i < $scope.edocta.length; i++) {
                var subt = $scope.edocta[i].gmmlp;
                var total = total + subt;
            }
            return total;
        }*/
        /*
        $scope.getTotal2 = function () {
            $scope.total = 0;
            for (var i = 0; i < $scope.edocta.length; i++) {
                var subt2 = parseFloat($scope.edocta[i].gmmlc);
                $scope.total = $scope.total + subt2;
                console.log($scope.total)
            }
        }*/
        /*
        $scope.getTotal3 = function () {
            var total3 = 0;
            for (var i = 0; i < $scope.edocta.length; i++) {
                var subt3 = $scope.edocta[i].autos;
                var total3 = total3 + subt3;
            }
            return total3;
        }*/
    });
    app.controller('estadistCtrl', function($scope, $http, $rootScope, $parse, ngDialog){
        $scope.reports = $rootScope.reports;
        //console.log($scope.reports)
        $scope.altaReport = function(report){
            $http.post('/rest/alta_report', report)
                .success(function (data, status, headers, config) {
                    $scope.reports.push(data);
                    //console.log(report.titulo);
                    report.titulo = " ";
                    report.url = " ";
                    report.descripcion = " ";
                });
            altaReportSuccess();
        }
        
        $scope.removeItem = function(index){
            var report = {id_report: $scope.reports[index].id_report}
            //console.log(report);
            $http.post('/rest/delete_report', report)
                .success(function(data, status, headers, config){
                    $scope.reports.splice(index, 1);
                    deleteReport();
            })
        }
        
        $scope.clickToOpen = function (report) {
            //console.log(report)
            ngDialog.open({
                template: '<iframe class="reports-frame" src='+ report.url +'></iframe>',
                plain: true,
                closeByDocument: false,
                className: 'ngdialog-theme-default',
                width: '95%',
                height: '130%'
            });
        };
    });
    app.controller('adminCatCtrl', function ($scope, $http, $rootScope, $parse) {
        $scope.tipoPagoList = $rootScope.tipo_pago;
        $scope.conceptoList = $rootScope.cat_concepto;
        $scope.detalleList = $rootScope.cat_detalle;
        //console.log($scope.tipoPagoList);
        //console.log($scope.conceptoList);
        //console.log($scope.detalleList);
    });
    app.controller('adminUsersCtrl', function ($scope, $rootScope, $log, $http, $routeParams, $location, $route) {
        $scope.catPerfiles = $rootScope.cat_perfiles;
        $scope.users = $rootScope.cat_users;
        $scope.catDirecciones = $rootScope.cat_direcc;
        $scope.catPuestos = $rootScope.cat_puestos;
        $scope.catAspectos = $rootScope.cat_aspectos;
        //console.log($scope.catPuestos)
        $scope.ban_user = 0;
        $scope.activarAltaUser = function () {
            $scope.ban_user = 1;
        };
        $scope.cancelaUser = function () {
            $scope.ban_user = 0;
        };
        $scope.altaUser = function (email,nombre,ap_pat,ap_mat,id_perfil,id_aspecto,id_puesto,id_direccion) {
            var user = {
                email: email,
                nombre: nombre,
                ap_pat: ap_pat,
                ap_mat: ap_mat,
                id_perfil: id_perfil,
                aspecto: id_aspecto,
                puesto: id_puesto,
                direccion: id_direccion
            };
            console.log(user)
            $http.post('/rest/alta_user', user)
                .success(function (data, status, headers, config) {
                    $scope.users.push(data);
                    console.log(data);
                });
            $scope.ban_user = 0;
            altaUserSuccess();
        };
    });
    app.controller('editUserCtrl', function ($scope, $rootScope, $log, $http, $routeParams, $location, $route) {
        $scope.catPerfiles = $rootScope.cat_perfiles;
        $scope.catDirecciones = $rootScope.cat_direcc;
        $scope.catPuestos = $rootScope.cat_puestos;
        $scope.catAspectos = $rootScope.cat_aspectos;
        
        for (var i = 0; i < $rootScope.cat_users.length; i++) {
            if ($rootScope.cat_users[i].id_usuario == $routeParams.id_usuario) {
                $scope.user = angular.copy($rootScope.cat_users[i]);
            }
        }
        console.log($scope.user)
        $scope.submitUpdate = function () {
            console.log($scope.user)
            $http.post('/rest/update_user', $scope.user)
                .success(function (data, status, headers, config) {
                    for (var i = 0; i < $rootScope.cat_users.length; i++) {
                        if ($rootScope.cat_users[i].id_usuario == $scope.user.id_usuario) {
                            $rootScope.cat_users.splice(i, 1);
                            break;
                        }
                    }
                    $rootScope.cat_users.push(data);
                    updateUserSuccess();
                });
            $location.path('/admin_usr');
        };


    });
    app.controller('adminFondCtrl', function ($scope, $rootScope, $log, $http, $routeParams, $location, $route, ngDialog) {
        var Fhoy = new Date();
        var Dhoy = Fhoy.getDate()
        console.log(Dhoy)
        /*if (Dhoy === 1){
            console.log("aqui va la notificación")
            ngDialog.open({
                template: '<h4>ESTA ES LA NOTIFICACION</h4>',
                plain: true,
                closeByDocument: false,
                className: 'ngdialog-theme-default',
                width: '95%',
                height: '130%'
            });
        }*/
        $scope.listFondos = $rootScope.cat_fondos;
        
  //RESET FONDOS MENSUALES//      
        $scope.resetFondos = function () {
                ngDialog.openConfirm({
                    template: 'modalDialogId',
                    className: 'ngdialog-theme-default',
                    width: '55%'
                }).then(function () {
                    console.log('continuar');
                    angular.forEach($scope.listFondos, function(value,key){
                        if (value.activo == 1){
                                if (value.mes == 12){
                                    var nuevoFondo = {
                                        user: value.id_func,
                                        ramo: value.id_ramo,
                                        linea_nego: value.id_linea_nego,
                                        monto: value.monto,
                                        mes: 1,
                                        year: value.year + 1,
                                    }
                                }
                                else {
                                    var nuevoFondo = {
                                        user: value.id_func,
                                        ramo: value.id_ramo,
                                        linea_nego: value.id_linea_nego,
                                        monto: value.monto,
                                        mes: value.mes + 1,
                                        year: value.year,
                                    } 
                                }
                                console.log(nuevoFondo)
                                $http.post('/rest/alta_fondo', nuevoFondo)
                                .success(function (data, status, headers, config) {
                                    $scope.listFondos.push(data);
                                    console.log(data);
                                });
                        }
                    })
                    catalogFondoSuccess();
                }, function (reason) {
                    console.log('cancelar');
                });
            };
 //RESET FONDOS MENSUALES//      
        
        //ACTUALIZAR FONDO//
        $scope.updateFondo = function (fondo) {
            $location.path('/update_fondo/' + fondo.id_fondo)
        };
        //ACTUALIZAR FONDO//
        
        //ACTIVAR FOM DE ALTA FONDO//
        $scope.activarAltaFondo = function () {
            $scope.ban_fondo = 1;
            var salida = [];
            angular.forEach($rootScope.cat_users, function (value, key) {
            if (value.id_perfil == 3) {
                salida.push(value);
            }
        })
        $scope.catFuncs = salida;
        var salida2 = [];
        angular.forEach($rootScope.ramo, function (value, key) {
            if (value.id_tipo_fae == 1) {
                salida2.push(value);
            }
        })
        $scope.catRamos = salida2;
        };
        //ACTIVAR FOM DE ALTA FONDO//
        
        //ALTA FONDO//
        $scope.altaFondo = function(id_user,id_ramo,id_linea_nego,mes,year,monto){
            var datFondo = {
                user: id_user,
                ramo: id_ramo,
                linea_nego: id_linea_nego,
                mes: mes,
                year: year,
                monto: monto
            }
            console.log(datFondo)
            $http.post('/rest/alta_fondo', datFondo)
                .success(function (data, status, headers, config) {
                    $scope.catFondos.push(data);
                    console.log(data);
                });
            $scope.ban_fondo = 0;
            altaFondoSuccess();
        };
        //ALTA FONDO//
        
        //BOTON CANCELAR FONDO//
        $scope.cancelaFondo = function(){
            $scope.ban_fondo = 0;
        };
        //BOTON CANCELAR FONDO//    
    });
    app.controller('editFondoCtrl', function ($scope, $rootScope, $log, $http, $routeParams, $location, $route) {
        $rootScope.navbarVal = 'activa';
        for (var i = 0; i < $rootScope.cat_fondos.length; i++) {
            if ($rootScope.cat_fondos[i].id_fondo == $routeParams.id_fondo) {
                $scope.fondo = angular.copy($rootScope.cat_fondos[i]);
            }
        }
        $scope.submitUpdateFondo = function () {
            $http.post('/rest/update_fondo', $scope.fondo)
                .success(function (data, status, headers, config) {
                    for (var i = 0; i < $rootScope.cat_fondos.length; i++) {
                        if ($rootScope.cat_fondos[i].id_fondo == $scope.fondo.id_fondo) {
                            $rootScope.cat_fondos.splice(i, 1);
                            break;
                        }
                    }
                    $rootScope.cat_fondos.push(data);
                    updateFondoSuccess();
                });
            $location.path('/admin_fond');
        };
    });
    app.controller('politCtrl', function ($scope,$rootScope, $timeout, $http, Upload, ngDialog, $window) {
        $scope.btnaddFile = true;
        $scope.listPoliticas = $rootScope.politicas
        //console.log($scope.listPoliticas)
        
        $scope.uploadFiles = function (files, errFiles) {
            $scope.btnaddFile = false;
            $scope.files = files;
            $scope.errFiles = errFiles;
            angular.forEach(files, function (file) {
                file.upload = Upload.upload({
                    url: 'rest/alta_polit',
                    data: {
                        file: file
                    }
                });

                file.upload.then(function (response) {
                    $timeout(function () {
                        file.result = response.data;
                        $scope.result2 = true;
                        console.log(response.data);
                        console.log("ya terminó");
                        altaPolitSuccess();
                        $timeout(function() {
                            $window.location.reload();
                        },2000);
                    });
                }, function (response) {
                    if (response.status > 0)
                        $scope.errorMsg = response.status + ': ' + response.data;
                }, function (evt) {
                    file.progress = Math.min(100, parseInt(100.0 *
                        evt.loaded / evt.total));
                });
            });
            /*
            altaPolitSuccess()
            $timeout(function() {
                $window.location.reload();
            },2000);*/
        }
        
        $scope.removePolit = function(index){
            var polit = {id_file: $scope.listPoliticas[index].id_file}
            //console.log(report);
            $http.post('/rest/delete_polit', polit)
                .success(function(data, status, headers, config){
                    $scope.listPoliticas.splice(index, 1);
                    deletePolitica();
            })
        }
    });
    /* controllers*/
    app.filter('filtroRamo', function () {
        return function (input, id_tipo_fae) {
            var salida = [];
            angular.forEach(input, function (ramo) {
                if (ramo.id_tipo_fae === id_tipo_fae) {
                    salida.push(ramo)
                }
            })
            return salida;
        }
    });
    app.filter('filtroTipoPago', function () {
        return function (input, id_ramo) {
            var salida = [];
            angular.forEach(input, function (tipo_pago) {
                if (tipo_pago.id_ramo === id_ramo && tipo_pago.activo === 1) {
                    salida.push(tipo_pago)
                }
            })
            return salida;
        }
    });
    app.filter('filtroConcepto', function () {
        return function (input, id_tipo_pago) {
            var salida = [];
            angular.forEach(input, function (concepto) {
                if (concepto.id_tipo_pago === id_tipo_pago) {
                    salida.push(concepto)
                }
            })
            return salida;
        }
    });
    app.filter('filtroMotivo', function () {
        return function (input, id_funcionario, id_func_vb) {
            var salida = [];
            angular.forEach(input, function (motivo) {
                if (motivo.id_func === id_funcionario || motivo.id_func === id_func_vb) {
                    salida.push(motivo)
                }
            })
            return salida;
        }
    });
    app.filter('filtroDetalle', function () {
        return function (input, id_motivo) {
            var salida = [];
            angular.forEach(input, function (detalle) {
                if (detalle.id_motivo === id_motivo) {
                    salida.push(detalle)
                }
            })
            return salida;
        }
    });
    app.filter('filtroEsp', function () {
        return function (input, id_tipo_fondo) {
            var salida = [];
            if (id_tipo_fondo === "1") {
                angular.forEach(input, function (func) {
                    if (func.puesto === "DIRECTOR" || func.puesto === "SUBDIRECTOR") {
                        salida.push(func)
                    }
                })
            } else if (id_tipo_fondo === "3") {
                angular.forEach(input, function (func) {
                    if (func.puesto === "DIRECTOR" || func.puesto === "SUBDIRECTOR") {
                        salida.push(func)
                    }
                })
            } else {
                angular.forEach(input, function (func) {
                    salida.push(func)
                })
            }
            return salida;
        }
    });
    app.filter('filtroMonto', function () {
        return function (input, id_ramo, id_linea_nego, id_funcionario) {
            var salida = [];
            angular.forEach(input, function (monto) {
                if (monto.id_ramo === id_ramo && monto.id_linea_nego === id_linea_nego && monto.id_funcionario === id_funcionario) {
                    salida.push(monto)
                }

            })
            return salida;
        }
    });
    /*filtross*/
