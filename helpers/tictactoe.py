import nextcord
from typing import List
from nextcord.ext import commands

class LookingForButton(nextcord.ui.Button):
    sep = '\u2001'

    def __init__(self, disabled: bool = False, label: str = None, user : nextcord.Member = None):
        self.user = user
        super().__init__(style=nextcord.ButtonStyle.blurple, label=(label or f'Join'), disabled=disabled, row=1)

    async def callback(self, interaction: nextcord.Interaction):
        assert self.view is not None
        view: LookingToPlay = self.view
        if interaction.user and interaction.user.id == view.ctx.author.id:
            return await interaction.response.send_message("You can't do that!", ephemeral=True)
        view.value = self.user
        view.stop()


class CancelGame(nextcord.ui.Button):
    def __init__(self, disabled : bool=False, label : str=None):
        super().__init__(label="Reject", style=nextcord.ButtonStyle.red, row=1, disabled=disabled)

    async def callback(self, interaction : nextcord.Interaction):
        assert self.view is not None
        view : LookingToPlay = self.view
        
        view.value = None
        
        for item in view.children:
            item.disabled = True
            item.label = item.label.replace("Cancel", "Cancelled!").replace("Join this game!\u2001", "The game has ended!")
        await view.message.edit(view=view)
        view.stop()
        	
class LookingToPlay(nextcord.ui.View):
    def __init__(self, timeout : int=120, label : str=None, user : nextcord.Member = None):
        super().__init__(timeout=timeout)
        self.message : nextcord.Message = None
        self.value : nextcord.User = None
        self.ctx : commands.Context = None
        self.add_item(LookingForButton(label=label, user=user))
        self.add_item(CancelGame())

    async def on_timeout(self) -> None:
        for button in self.children:
            button.disabled = True
            button.label = button.label.replace("Join this game!\u2001", "The game timed out!")
        await self.message.edit(content=":alarm_clock: Timed out! The game has ended!", view=self)
		
class TicTacToeButton(nextcord.ui.Button['TicTacToe']):
    def __init__(self, x : int, y : int):
        super().__init__(label='  ', style=nextcord.ButtonStyle.secondary, row=y)
        self.x = x
        self.y = y

    async def callback(self, interaction : nextcord.Interaction):
        assert self.view is not None
        view: TicTacToe = self.view
        state = view.board[self.y][self.x]
        if state in (view.X, view.O):
            return

        if view.current_player == view.player1:
            self.style = nextcord.ButtonStyle.blurple
            self.label = '❎'
            self.disabled = True
            view.board[self.y][self.x] = view.X
            
        else:
            self.style = nextcord.ButtonStyle.red
            self.label = '🅾️'
            self.disabled = True
            view.board[self.y][self.x] = view.O

        winner = view.check_board_winner()
        if winner is not None:
            
            if winner == view.X:
                content = f"\U0001f1fd :tada: __**{view.current_player.name} WON!!!**__ :tada:"
                
            elif winner == view.O:
                content = f"🅾 :tada: __**{view.current_player.name} WON!!!**__ :tada:"
                
            else:
                content = f"\U0001f454 It's a tie!"

            for child in view.children:
                child.disabled = True

            view.stop()

        else:
            
            if view.current_player == view.player1:
                view.current_player = view.player2
                content = f"🅾 It's {view.current_player.name}'s turn"
                
            else:
                view.current_player = view.player1
                content = f"\U0001f1fd It's {view.current_player.name}'s turn"

        await interaction.response.edit_message(content=content, view=view)


class TicTacToe(nextcord.ui.View):
    children: List[TicTacToeButton]
    X = -1
    O = 1
    Tie = 2

    def __init__(self, ctx, player1 : nextcord.Member, player2 : nextcord.Member, starter : nextcord.User):
        super().__init__()
        self.current_player = starter
        self.ctx : commands.Context = ctx
        self.player1 : nextcord.Member = player1
        self.player2 : nextcord.Member = player2
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

        for x in range(3):
            for y in range(3):
                self.add_item(TicTacToeButton(x, y))

    def check_board_winner(self):
        for across in self.board:
            value = sum(across)
            if value == 3:
                return self.O
            elif value == -3:
                return self.X

        for line in range(3):
            value = self.board[0][line] + self.board[1][line] + self.board[2][line]
            if value == 3:
                return self.O
            elif value == -3:
                return self.X

        diag = self.board[0][2] + self.board[1][1] + self.board[2][0]
        if diag == 3:
            return self.O
        elif diag == -3:
            return self.X

        diag = self.board[0][0] + self.board[1][1] + self.board[2][2]
        if diag == 3:
            return self.O
        elif diag == -3:
            return self.X

        if all(i != 0 for row in self.board for i in row):
            return self.Tie

        return None

    async def interaction_check(self, interaction: nextcord.Interaction) -> bool:
        if interaction.user and interaction.user.id == self.current_player.id:
            return True
        
        elif interaction.user and interaction.user.id in (self.player1.id, self.player2.id):
            await interaction.response.send_message("It's not your turn!", ephemeral=True)
            
        elif interaction.user:
            await interaction.response.send_message("You aren't a part of this game!", ephemeral=True)
            
        return False