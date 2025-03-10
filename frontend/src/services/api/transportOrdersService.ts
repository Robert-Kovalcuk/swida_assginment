import type { TransportOrder } from '@/services/api/data/TransportOrder.ts'
import Fetch from '@/services/fetch.ts'

export default class TransportOrdersService {
    public static async getTransportOrders(customer?: string): Promise<TransportOrder[]> {
        return await Fetch.get<TransportOrder[]>('/transport_orders/' + `${customer ? `?customer_name=${customer}` : ''}`)
    }

    public static async createTransportOrder(transportOrder: TransportOrder): Promise<TransportOrder> {
        return await Fetch.post<TransportOrder, TransportOrder>('/transport_orders/', transportOrder)
    }

    public static async updateTransportOrder(transportOrder: TransportOrder): Promise<TransportOrder> {
        return await Fetch.put<TransportOrder, TransportOrder>('/transport_orders/', transportOrder)
    }
}
