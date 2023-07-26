import 'dotenv/config'
import pokemon from 'pokemontcgsdk'

pokemon.configure({ apiKey: process.env.API_KEY })

// return single card obj
function findCardById(card_id) {
	pokemon.card.find(card_id).then((card) => {
		return card
	})
}

// return multiple card obj
async function findCardsByParams(query) {
	try {
		const obj = await pokemon.card.all({
			q: query,
		})
		return obj
	} catch (error) {
		console.error('Error:', error.message)
		throw error
	}
}

// Function to filter cards by id
function filterCardsById(cardsArray, targetId) {
	return cardsArray.filter((card) => card.id === targetId)
}

export { findCardById, findCardsByParams }
;(async () => {
	try {
		const cards = await findCardsByParams('name:blastoise')
		const filteredCards = filterCardsById(cards, 'pgo-18')
		console.log(filteredCards[0].types[0])
	} catch (error) {
		console.error('Error:', error.message)
	}
})()
