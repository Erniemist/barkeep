import discord

from src.avalon import proposal
from src.avalon.proposal_select import ProposalSelect
from src.avalon.game import load_players
from src.discord.client.client_interface import ClientInterface


class ProposalView(discord.ui.View):
    def __init__(self, proposal_select: ProposalSelect):
        super().__init__()
        self.add_item(proposal_select)
        self.confirm.disabled = True

    @discord.ui.button(label="confirm", disabled=True)
    async def confirm(self, interaction: discord.Interaction, _):
        select = self.children[1]
        assert isinstance(select, ProposalSelect)

        await proposal.submit_proposal(interaction, select.values)


async def make(client: ClientInterface):
    players = await load_players(client)
    return ProposalView(ProposalSelect(players))
