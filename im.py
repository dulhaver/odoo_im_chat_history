from openerp.osv import fields,osv

class im_history(osv.osv):
        _inherit = 'im_chat.message'
im_history()
im_view.xml
<?xml version="1.0" encoding="utf-8"?>
    <openerp>
        <data>
            <record id="view_im_history" model="ir.ui.view">
                <field name="name">im_chat.message.tree</field>
                <field name="model">im_chat.message</field>
                <field name="arch" type="xml">
                    <tree string="IM">
                        <field name="create_date"/>
                        <field name="from_id"/>
                        <field name="to_id"/>
                        <field name="message"/>
                    </tree>
                </field>
            </record>

    <!-- Top menu item -->
    <menuitem name="IM"
    id="im_history_root"
    groups="base.group_user"
    sequence="10"/>
    <record id="open_view_im_history" model="ir.actions.act_window">
        <field name="name">Instant messaging history</field>
        <field name="res_model">im_chat.message</field>
        <field name="view_type">form</field>
        <field name="view_mode">tree</field>
        <field name="view_id" ref="view_im_history"/>
    </record>

    <menuitem name="Actions" id="im_history" parent="im_history_root" groups="base.group_user"/>
    <menuitem action="open_view_im_history" id="menu_open_view_im_history" parent="im_history" sequence="20" groups="base.group_user"/>
    </data>
</openerp>
