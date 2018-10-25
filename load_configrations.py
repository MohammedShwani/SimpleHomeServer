class Config:
    __configFilePath = '.env'
    __configList = {
        'SERV_ADDRESS':'', 'SERV_NAME':'', 'SERV_PORT':'', 'SERV_ROOT_PATH':''
    }

    def get(self, configName):
        return self.__configList[configName]

    def load(self):
        with open(self.__configFilePath) as fp:
            for cnt, line in enumerate(fp):
                line = line.strip()#remove all spaces from start and end

                #if line is empty, ignore it
                if len(line) == 0:
                    continue
                
                #separate config name from its value
                config = line.split('=')

                #make sure config length equal to two (name+value)
                if (len(config) != 2):
                    raise Exception('Faild to parse .env file, please check it !!!')

                #strip name and value from spaces
                config[0] = config[0].strip()
                config[1] = config[1].strip()

                #make sure config name exist in configrations list
                if config[0] not in self.__configList:
                    raise Exception('Faild to parse .env file, please check it !!!')

                #if config value starts with " or ', make sure it ends with it as well
                #this only happens if leng is equal or bigger than 2
                #also remove the ' or " if exist
                if (len(config[1]) >= 2):
                    config[1] = self.__removeQuotes(config[1])

                #set config value
                self.__configList[config[0]] = config[1]

    def __removeQuotes(self, str):
        if str[0] == '\'':
            if str[-1] != '\'':
                raise Exception('Faild to parse .env file, please check it !!!')
            return str[1:-1]
        elif str[0] == '"':
            if str[0] != '"':
                raise Exception('Faild to parse .env file, please check it !!!')
            return str[1:-1]
        
        return str

