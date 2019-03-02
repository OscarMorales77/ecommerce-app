# Generated by Django 2.0.3 on 2019-02-24 22:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PastaOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Pasta Order',
            },
        ),
        migrations.CreateModel(
            name='PastaPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'verbose_name_plural': 'Pasta Price',
            },
        ),
        migrations.CreateModel(
            name='PendingOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Pending Orders',
            },
        ),
        migrations.CreateModel(
            name='PizzaOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Pizza Order',
            },
        ),
        migrations.CreateModel(
            name='PizzaPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification', models.CharField(max_length=10)),
                ('size', models.CharField(max_length=10)),
                ('num_toppings', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'verbose_name_plural': 'Pizza Price',
            },
        ),
        migrations.CreateModel(
            name='PlatterOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Platter Order',
            },
        ),
        migrations.CreateModel(
            name='PlatterPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification', models.CharField(max_length=30)),
                ('size', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'verbose_name_plural': 'Platter Price',
            },
        ),
        migrations.CreateModel(
            name='SaladOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Salad Order',
            },
        ),
        migrations.CreateModel(
            name='SaladPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'verbose_name_plural': 'Salad Price',
            },
        ),
        migrations.CreateModel(
            name='ShoppingCartOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Shopping Cart',
            },
        ),
        migrations.CreateModel(
            name='SubOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Sub Order',
            },
        ),
        migrations.CreateModel(
            name='SubPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification', models.CharField(max_length=30)),
                ('size', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'verbose_name_plural': 'Sub Price',
            },
        ),
        migrations.CreateModel(
            name='Toppings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Pizza Toppings',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pending_orders', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='pending', to='orders.PendingOrders')),
                ('shooping_cart', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='orders.ShoppingCartOrders')),
            ],
        ),
        migrations.AddField(
            model_name='suborder',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subOrder', to='orders.UserProfile'),
        ),
        migrations.AddField(
            model_name='suborder',
            name='price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subOrder', to='orders.SubPrice'),
        ),
        migrations.AddField(
            model_name='shoppingcartorders',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.UserProfile'),
        ),
        migrations.AddField(
            model_name='shoppingcartorders',
            name='pasta_order',
            field=models.ManyToManyField(blank=True, to='orders.PastaOrder'),
        ),
        migrations.AddField(
            model_name='shoppingcartorders',
            name='pizza_order',
            field=models.ManyToManyField(blank=True, to='orders.PizzaOrder'),
        ),
        migrations.AddField(
            model_name='shoppingcartorders',
            name='platter_order',
            field=models.ManyToManyField(blank=True, to='orders.PlatterOrder'),
        ),
        migrations.AddField(
            model_name='shoppingcartorders',
            name='salad_order',
            field=models.ManyToManyField(blank=True, to='orders.SaladOrder'),
        ),
        migrations.AddField(
            model_name='shoppingcartorders',
            name='sub_order',
            field=models.ManyToManyField(blank=True, to='orders.SubOrder'),
        ),
        migrations.AddField(
            model_name='saladorder',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saladOrder', to='orders.UserProfile'),
        ),
        migrations.AddField(
            model_name='saladorder',
            name='price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saladOrder', to='orders.SaladPrice'),
        ),
        migrations.AddField(
            model_name='platterorder',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='platterOrder', to='orders.UserProfile'),
        ),
        migrations.AddField(
            model_name='platterorder',
            name='price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='platterOrder', to='orders.PlatterPrice'),
        ),
        migrations.AddField(
            model_name='pizzaorder',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizzaOrder', to='orders.UserProfile'),
        ),
        migrations.AddField(
            model_name='pizzaorder',
            name='price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizzaOrder', to='orders.PizzaPrice'),
        ),
        migrations.AddField(
            model_name='pizzaorder',
            name='topping',
            field=models.ManyToManyField(blank=True, to='orders.Toppings'),
        ),
        migrations.AddField(
            model_name='pendingorders',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.UserProfile'),
        ),
        migrations.AddField(
            model_name='pendingorders',
            name='pasta_order',
            field=models.ManyToManyField(blank=True, to='orders.PastaOrder'),
        ),
        migrations.AddField(
            model_name='pendingorders',
            name='pizza_order',
            field=models.ManyToManyField(blank=True, to='orders.PizzaOrder'),
        ),
        migrations.AddField(
            model_name='pendingorders',
            name='platter_order',
            field=models.ManyToManyField(blank=True, to='orders.PlatterOrder'),
        ),
        migrations.AddField(
            model_name='pendingorders',
            name='salad_order',
            field=models.ManyToManyField(blank=True, to='orders.SaladOrder'),
        ),
        migrations.AddField(
            model_name='pendingorders',
            name='sub_order',
            field=models.ManyToManyField(blank=True, to='orders.SubOrder'),
        ),
        migrations.AddField(
            model_name='pastaorder',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pastaOrder', to='orders.UserProfile'),
        ),
        migrations.AddField(
            model_name='pastaorder',
            name='price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pastaOrder', to='orders.PastaPrice'),
        ),
    ]
