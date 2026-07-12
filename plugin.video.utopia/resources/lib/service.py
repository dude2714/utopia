from entry import logger, UtopiaMonitor

if __name__ == '__main__':
	logger('Utopia', 'Main Monitor Service Starting')
	logger('Utopia', 'Settings Monitor Service Starting')

	with UtopiaMonitor() as Utopia:
		Utopia.startUpServices()
		Utopia.waitForAbort()

	logger('Utopia', 'Settings Monitor Service Finished')
	logger('Utopia', 'Main Monitor Service Finished')


