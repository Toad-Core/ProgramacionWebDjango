$(document).ready(function () {
    const $formulario = $("#registroTalento");
    const $btnEnviar = $("#btn-enviar");

    const modal = new bootstrap.Modal(
        $("#modalConfirmacion")[0]
    );

    const reglas_Validacion = {
        nombre: {
            presence: {
                allowEmpty: false,
                message: "es obligatorio"
            },
            length: {
                minimum: 2,
                message: "debe tener al menos 2 caracteres"
            }
        },

        apellido: {
            presence: {
                allowEmpty: false,
                message: "es obligatorio"
            }
        },

        edad: {
            presence: true,
            numericality: {
                greaterThanOrEqualTo: 5,
                lessThanOrEqualTo: 19,
                message: "debe estar entre 5 y 19"
            }
        },

        curso: {
            presence: {
                allowEmpty: false,
                message: "debe seleccionar un curso"
            }
        },

        categoria: {
            presence: {
                allowEmpty: false,
                message: "debe seleccionar una categoría"
            }
        },

        descripcion: {
            presence: true,
            length: {
                minimum: 10,
                message: "debe tener mínimo 10 caracteres"
            }
        },

        apoderado: {
            presence: true
        },

        correoApoderado: {
            presence: true,
            email: {
                message: "no es válido"
            }
        },

        telefonoApoderado: {
            presence: true,
            format: {
                pattern: "^[0-9+ ]+$",
                message: "solo puede contener números"
            }
        }
    };

    function mostrarError($input, errores) {

        $input.removeClass("is-valid");
        $input.addClass("is-invalid");

        let $feedback = $input.siblings(".invalid-feedback");

        if (!$feedback.length) {
            $feedback = $("<div>")
                .addClass("invalid-feedback");
            $input.after($feedback);
        }

        $feedback.text(errores[0]);
    }

    function mostrarValido($input) {
        $input.removeClass("is-invalid");
        $input.addClass("is-valid");
    }

    function validarInput(input) {

        const $input = $(input);
        const nombre = $input.attr("id");
        const valor = $input.val();
        const valores_formulario = {};
        valores_formulario[nombre] = valor;

        const reglas = {};
        reglas[nombre] = reglas_Validacion[nombre];
        const errores = validate(valores_formulario, reglas);

        if (errores) {
            mostrarError($input, errores[nombre]);
            return false;
        }
        mostrarValido($input);
        return true;
    }


    function validarFormulario() {
        let valido = true;

        $("input, select, textarea").each(function () {
            if (!validarInput(this)) {
                valido = false;
            }
        });

        $btnEnviar.prop("disabled", !valido);
        return valido;
    }


    function cambiarTab(tabId) {
        const tab = new bootstrap.Tab($(tabId)[0]);
        tab.show();
    }


    $("input, select, textarea").on("blur change", function () {
        validarInput(this);
        validarFormulario();
    });


    $("#next1").click(function () {
        const ok =
            validarInput($("#nombre")) &
            validarInput($("#apellido")) &
            validarInput($("#edad")) &
            validarInput($("#curso"));

        if (!ok) return;
        $("#tab2-btn").prop("disabled", false);

        cambiarTab("#tab2-btn");
    });

    $("#next2").click(function () {

        const ok =
            validarInput($("#categoria")) &
            validarInput($("#descripcion"));

        if (!ok) return;
        $("#tab3-btn").prop("disabled", false);
        cambiarTab("#tab3-btn");
    });

    $("#back2").click(function () {
        cambiarTab("#tab1-btn");
    });

    $("#back3").click(function () {
        cambiarTab("#tab2-btn");
    });

    $formulario.submit(function (e) {
        e.preventDefault();
        if (!validarFormulario()) return;
        modal.show();
    });


    $("#btnConfirmar").click(function () {
        modal.hide();
        $formulario[0].reset();

        $(".form-control, .form-select")
        .removeClass("is-valid is-invalid");
        $(".invalid-feedback").remove();
        $("#tab2-btn, #tab3-btn")
        .prop("disabled", true);

        $btnEnviar.prop("disabled", true);
        cambiarTab("#tab1-btn");
    });

});