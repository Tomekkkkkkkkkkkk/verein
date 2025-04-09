from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import pandas as pd
import os
from datetime import datetime
from reportlab.pdfgen import canvas
from forum import forum_bp

app = Flask(__name__)
app.secret_key = 'supersecretkey'
UPLOAD_FOLDER = 'data/uploads'
PDF_FOLDER = 'data/rechnungen'

app.register_blueprint(forum_bp)

# (Restlicher Code kann hier ergänzt werden)
