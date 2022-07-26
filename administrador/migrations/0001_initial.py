# Generated by Django 4.0.4 on 2022-06-02 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdjuntarArchivos',
            fields=[
                ('iddocumento', models.AutoField(primary_key=True, serialize=False)),
                ('registro_fotografico', models.TextField()),
                ('soat', models.TextField()),
                ('tecnomecanico', models.TextField()),
                ('identificacion_propietario', models.TextField()),
                ('tarjeta_propiedad', models.TextField()),
            ],
            options={
                'db_table': 'adjuntar_archivos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CargarDocumento',
            fields=[
                ('iddocumento', models.AutoField(primary_key=True, serialize=False)),
                ('certificado_alcoholemia', models.TextField()),
                ('certificado_sustancias_psicoactivas', models.TextField()),
            ],
            options={
                'db_table': 'cargar_documento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('idconductor', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('correo_electronico', models.CharField(max_length=30)),
                ('tipo_identificacion', models.CharField(max_length=20)),
                ('numero_identificacion', models.PositiveIntegerField()),
                ('fecha_expedicion_documento', models.DateField()),
                ('lugar_expedicion_documento', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField()),
                ('edad', models.PositiveIntegerField()),
                ('direccion', models.CharField(max_length=20)),
                ('telefono', models.PositiveIntegerField()),
                ('telefono_alterno', models.PositiveIntegerField()),
                ('turno_idturno', models.PositiveIntegerField()),
                ('subir_archivos_iddocumento', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'conductor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DescargarRodamiento',
            fields=[
                ('iddescargar', models.AutoField(primary_key=True, serialize=False)),
                ('documento', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'descargar_rodamiento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ImprimirRodamiento',
            fields=[
                ('idimprimir_rodamiento', models.AutoField(primary_key=True, serialize=False)),
                ('documento', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'imprimir_rodamiento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Paradero',
            fields=[
                ('idparadero', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('ubicacion_idubicacion', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'paradero',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Permisos',
            fields=[
                ('idpermisos', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_permiso', models.CharField(max_length=70)),
                ('descripcion', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'permisos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PlanRodamiento',
            fields=[
                ('idplan_rodamiento', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('inicio_ruta', models.CharField(max_length=30)),
                ('vehiculo', models.PositiveIntegerField(blank=True, null=True)),
                ('ruta', models.PositiveIntegerField(blank=True, null=True)),
                ('vehiculo_idvehiculo', models.PositiveIntegerField()),
                ('ruta_idruta', models.PositiveIntegerField()),
                ('cargar_documento_iddocumento', models.IntegerField()),
                ('imprimir_rodamiento_idimprimir_rodamiento', models.PositiveIntegerField()),
                ('descargar_rodamiento_iddescargar', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'plan_rodamiento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('idrol', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_rol', models.CharField(max_length=70)),
                ('permisos_idpermisos', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'rol',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('idruta', models.AutoField(primary_key=True, serialize=False)),
                ('inicio_ruta', models.CharField(max_length=30)),
                ('fin_ruta', models.CharField(max_length=30)),
                ('numero_ruta', models.PositiveIntegerField()),
                ('distancia_kilometros', models.PositiveIntegerField()),
                ('tiempo_estimado', models.TimeField(blank=True, null=True)),
                ('numero_vueltas', models.PositiveIntegerField(blank=True, null=True)),
                ('vehiculo_idvehiculo', models.PositiveIntegerField()),
                ('paradero_idparadero', models.PositiveIntegerField()),
                ('usuario_idusuario', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'ruta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SubirArchivos',
            fields=[
                ('iddocumento', models.AutoField(primary_key=True, serialize=False)),
                ('documento_identidad', models.TextField()),
                ('experiencia_laboral', models.TextField()),
                ('licencia_conduccion', models.TextField()),
            ],
            options={
                'db_table': 'subir_archivos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('idturno', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=15)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
            ],
            options={
                'db_table': 'turno',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('idubicacion', models.AutoField(primary_key=True, serialize=False)),
                ('longitud', models.FloatField()),
                ('latitud', models.FloatField()),
            ],
            options={
                'db_table': 'ubicacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idusuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('tipo_documento', models.CharField(max_length=45)),
                ('numero_documento', models.CharField(max_length=45)),
                ('telefono', models.CharField(max_length=45)),
                ('correo_electronico', models.CharField(max_length=70)),
                ('contrasena', models.CharField(max_length=8)),
                ('rol_idrol', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('idvehiculo', models.AutoField(primary_key=True, serialize=False)),
                ('numero_orden', models.PositiveIntegerField()),
                ('numero_licencia_transito', models.PositiveIntegerField()),
                ('nombre_propietario', models.CharField(max_length=45)),
                ('identificacion_propietario', models.PositiveIntegerField()),
                ('placa', models.CharField(max_length=10)),
                ('marca', models.CharField(max_length=20)),
                ('linea', models.CharField(max_length=20)),
                ('modelo', models.PositiveIntegerField()),
                ('capacidad_personas', models.PositiveIntegerField()),
                ('clase_vehiculo', models.CharField(max_length=20)),
                ('cilindraje', models.FloatField()),
                ('numero_chasis', models.CharField(max_length=20)),
                ('tipo_combustible', models.CharField(max_length=10)),
                ('numero_motor', models.CharField(max_length=20)),
                ('tipo_carroceria', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('vin', models.CharField(max_length=20)),
                ('numero_ejes', models.IntegerField()),
                ('conductor_idconductor', models.PositiveIntegerField()),
                ('adjuntar_archivos_iddocumento', models.IntegerField()),
                ('ubicacion_idubicacion', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'vehiculo',
                'managed': False,
            },
        ),
    ]
