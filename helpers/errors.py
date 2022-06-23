from nextcord.ext import commands

class UnknownError(commands.CheckFailure):
    def __init__(self):
        message = "An unknown error has occured."
        super().__init__(message)

class CommandDoesntExist(commands.CheckFailure):
    def __init__(self):
        message = "The command you're trying to use doesn't exist."
        super().__init__(message)

class AuthorBlacklisted(commands.CheckFailure):
    def __init__(self):
        message = "You're blacklisted from using this bot."
        super().__init__(message)

class Forbidden(commands.CheckFailure):
    def __init__(self):
        message = "You don't have permission to use this command."
        super().__init__(message)

class BotMaintenance(commands.CheckFailure):
    def __init__(self):
        message = "The bot is currently undergoing maintenance."
        super().__init__(message)

class NoBannedMembers(commands.CheckFailure):
    def __init__(self):
        message = "There are no banned members."
        super().__init__(message)

class TooLongPrefix(commands.CheckFailure):
    def __init__(self):
        message = "The prefix you entered is too long."
        super().__init__(message)

class EmptyTodoList(commands.CheckFailure):
    def __init__(self):
        message = "The todo list is empty."
        super().__init__(message)

class NoSpotifyStatus(commands.CheckFailure):
    def __init__(self):
        message = "There is no status set for Spotify."
        super().__init__(message)

class InvalidThread(commands.CheckFailure):
    def __init__(self):
        message = "The thread you're trying to use is invalid."
        super().__init__(message)

class TooManyPrefixes(commands.CheckFailure):
    def __init__(self):
        message = "Too many prefixes."
        super().__init__(message)

class PrefixAlreadyExists(commands.CheckFailure):
    def __init__(self):
        message = "That prefix already exists."
        super().__init__(message)

class PrefixDoesntExist(commands.CheckFailure):
    def __init__(self):
        message = "That prefix doesn't exist."
        super().__init__(message)

class InvalidError(commands.CheckFailure):
    def __init__(self):
        message = "Invalid error."
        super().__init__(message)

########################################################################################################################
##### MUTE ROLE ERRORS #####
########################################################################################################################

class MuteRoleNotFound(commands.CheckFailure):
    def __init__(self):
        message = "The mute role doesn't exist."
        super().__init__(message)

class MuteRoleAlreadyExists(commands.CheckFailure):
    def __init__(self):
        message = "The mute role already exists."
        super().__init__(message)