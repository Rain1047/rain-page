from dashboardapp import app

import os
import configparser
# dashboardapp
config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))

if __name__ == '__main__':
    # app.config['MONGO_URL'] = config['PROD']['DB_URI']
    app.run(host='0.0.0.0', port=3001, debug=True)